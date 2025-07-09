import os
from django.conf import settings
import re
from functools import lru_cache


# Modelos
from apps.utils.models import ValorSistema
from apps.utils.models import Region, Comuna, Provincia

# Contrib
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from datetime import datetime, date, time, timedelta

# Funciones
# -------------------------------------------------------
# TODO: LIMPIADORES
# -------------------------------------------------------
def limpiar_numeros_decimal(valor):
    """
    Limpia el valor ingresado y lo transforma a decimal
    """
    if isinstance(valor, (list, tuple)) and len(valor) == 1:
        valor = valor[0]

    if not valor:
        return Decimal('0')
    valor = re.sub(r'[^0-9,]', '', str(valor))
    valor = valor.replace(',', '.')
    try:
        return Decimal(valor)
    except InvalidOperation:
        return Decimal('0')

def limpiar_numeros_entero(valor):
    """
    Limpia el valor ingresado y lo transforma a entero, si es decimal lo redondea
    """
    if isinstance(valor, (list, tuple)) and len(valor) == 1:
        valor = valor[0]

    if not valor:
        return 0
    valor = re.sub(r'[^\d,\.]', '', str(valor))
    valor = valor.replace(',', '.')
    try:
        decimal_val = Decimal(valor)
        return int(decimal_val.to_integral_value(rounding=ROUND_HALF_UP))
    except (ValueError, InvalidOperation):
        return 0
    
def limpiar_texto(texto):
    """
    Limpia el valor ingresado y retorna solo texto
    """
    if isinstance(texto, (list, tuple)) and len(texto) == 1:
        texto = texto[0]

    if not texto:
        return ""
    texto = re.sub(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ\s]', '', str(texto))
    texto = re.sub(r'\d+', '', texto)
    return texto.strip()

def limpiar_fecha(texto, tipo='date'):
    """
    Convierte un string en fecha, datetime, hora o duración.
    tipo puede ser: 'date', 'datetime', 'time', 'duration'
    """
    if isinstance(texto, (list, tuple)) and len(texto) == 1:
        texto = texto[0]

    if not texto or not isinstance(texto, str):
        return None

    texto = texto.strip()

    # Formatos válidos
    formatos_fecha = ["%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y", "%d.%m.%Y"]
    formatos_datetime = ["%d-%m-%Y %H:%M", "%d-%m-%Y %H:%M:%S", "%Y-%m-%d %H:%M:%S"]
    formatos_hora = ["%H:%M", "%H:%M:%S"]

    try:
        if tipo == "date":
            for fmt in formatos_fecha:
                try:
                    return datetime.strptime(texto, fmt).date()
                except ValueError:
                    continue

        elif tipo == "datetime":
            for fmt in formatos_datetime:
                try:
                    return datetime.strptime(texto, fmt)
                except ValueError:
                    continue

        elif tipo == "time":
            for fmt in formatos_hora:
                try:
                    return datetime.strptime(texto, fmt).time()
                except ValueError:
                    continue

        elif tipo == "duration":
            # Ejemplo: "2h 30m" o "01:45:00"
            match = re.match(r'(?:(\d+)h)?\s*(?:(\d+)m)?', texto)
            if match:
                horas = int(match.group(1) or 0)
                minutos = int(match.group(2) or 0)
                return timedelta(hours=horas, minutes=minutos)

            # Alternativa: formato HH:MM:SS
            partes = texto.split(":")
            if len(partes) == 2:
                horas, minutos = map(int, partes)
                return timedelta(hours=horas, minutes=minutos)
            elif len(partes) == 3:
                horas, minutos, segundos = map(int, partes)
                return timedelta(hours=horas, minutes=minutos, seconds=segundos)

    except Exception as e:
        print(f"[Error] No se pudo limpiar '{texto}' como tipo '{tipo}': {e}")
        return None
    
def parse_repeater_data(post_data, prefix="caracteristica"):
    """
    Extrae y estructura datos de tipo repeater desde un QueryDict (request.POST).
    """
    raw_data = {}
    pattern = re.compile(rf"^{re.escape(prefix)}\[(\d+)\]\[(\w+)\]$")

    for key, value in post_data.items():
        match = pattern.match(key)
        if match:
            index = int(match.group(1))
            field = match.group(2)
            if index not in raw_data:
                raw_data[index] = {}
            raw_data[index][field] = value.strip()

    # Convertir a lista
    data_list = [
        item for item in raw_data.values()
        if item.get("nombre") or item.get("descripcion")
    ]
    return data_list
    
def limpiar_unidad_duracion(duracion, unidad_duracion):
    """
    Recibe una duración (int) y una instancia de ValorSistema,
    y devuelve la unidad corregida según sea singular o plural.
    """
    if not unidad_duracion:
        return None
    clave = unidad_duracion.clave.lower()

    excepciones_plural_a_singular = {
        "días": "día",
        "semanas": "semana",
        "meses": "mes",
        "años": "año"
    }
    excepciones_singular_a_plural = {v: k for k, v in excepciones_plural_a_singular.items()}

    if duracion == 1 and clave in excepciones_plural_a_singular:
        singular = excepciones_plural_a_singular[clave]
        return ValorSistema.objects.filter(clave=singular, grupo__nombre="tiempo").first()

    elif duracion > 1 and clave in excepciones_singular_a_plural:
        plural = excepciones_singular_a_plural[clave]
        return ValorSistema.objects.filter(clave=plural, grupo__nombre="tiempo").first()

    return unidad_duracion

# -------------------------------------------------------
# TODO: VALIDACIONES
# -------------------------------------------------------
def validar_rut(rut):
    if isinstance(rut, (list, tuple)) and len(rut) == 1:
        rut = rut[0]

    rut = str(rut).strip().upper().replace(".", "").replace("-", "")
    
    if not re.match(r'^\d{7,8}[0-9K]$', rut):
        return False

    cuerpo = rut[:-1]
    dv = rut[-1]

    suma = 0
    multiplo = 2
    for c in reversed(cuerpo):
        suma += int(c) * multiplo
        multiplo = 2 if multiplo == 7 else multiplo + 1

    resto = suma % 11
    dv_calc = 11 - resto
    if dv_calc == 11:
        dv_esperado = '0'
    elif dv_calc == 10:
        dv_esperado = 'K'
    else:
        dv_esperado = str(dv_calc)

    return dv == dv_esperado

def validar_telefono(telefono):
    """
    Limpia y valida un numero de telefono chileno
    """
    if not telefono:
        raise ValueError("El numero no puede estar vacio")
    
    telefono_limpio = re.sub(r'[^\d]', '', str(telefono))
    if not re.fullmatch(r'9\d{8}', telefono_limpio):
        raise ValueError("El número debe tener 9 dígitos y comenzar con 9 (ej: 912312312)")
    
    return telefono_limpio

def validar_fecha(fecha, tipo='date'):
    if isinstance(fecha, (list, tuple)) and len(fecha) == 1:
        fecha = fecha[0]
    if not fecha:
        raise ValueError("Debe ingresar una fecha.")
    
    
    fecha_limpia = limpiar_fecha(str(fecha), tipo=tipo)
    if not fecha_limpia:
        raise ValueError("La fecha ingresada no es válida.")
    
    return fecha_limpia

def validar_porcentaje(porcentaje):
    """
    Limpia y valida que un valor sea un porcentaje válido entre 0 y 100.
    """
    if isinstance(porcentaje, (list, tuple)) and len(porcentaje) == 1:
        porcentaje = porcentaje[0]

    valor = limpiar_numeros_decimal(porcentaje)

    if valor < 0 or valor > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100.")

    return valor

# -------------------------------------------------------
# TODO: CALCULOS
# -------------------------------------------------------

# -------------------------------------------------------
# TODO: GET GENERALES
# -------------------------------------------------------
def get_all_comunas():
    return Comuna.objects.all().order_by('id')

def get_all_provincias():
    return Provincia.objects.all().order_by('id')

def get_all_regiones():
    return Region.objects.all().order_by('id')

def get_iva(iva, subtotal):
    if iva <= 0:
        return subtotal
    if iva < 1:
        descuento_total = 100 - descuento
        return subtotal * descuento_total
    else:
        descuento = descuento/100
        descuento_total = 100 - descuento
        return subtotal * descuento_total

@lru_cache(maxsize=1)
def get_all_icon():
    """ Devuelve una lista con los iconos definidos y los guarda en un archivo de texto """
    css_path = os.path.join(settings.BASE_DIR, 'src', 'assets', 'vendor', 'fonts', 'remixicon', 'remixicon.css')

    if not os.path.exists(css_path):
        return []

    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()

    # Buscar todas las clases .ri-xxxxx:before
    icon_classes = re.findall(r"\.ri-([a-z0-9\-]+):before", css_content, re.IGNORECASE)

    # Filtrar clases válidas (quitar clases de tamaño, espaciado, etc.)
    excluded_patterns = re.compile(r'^\d+x$|^(sm|lg|fw|xl|xs|xxs|[0-9]+px)$', re.IGNORECASE)
    filtered_icons = sorted(set(f"ri-{cls}" for cls in icon_classes if not excluded_patterns.match(cls)))


    return sorted(set(filtered_icons))

def get_suma(valor_1, valor_2):
    return valor_1 + valor_1
