# Renderizacion
from django.template.loader import render_to_string
from django.http import JsonResponse
from decimal import Decimal, InvalidOperation
from django.shortcuts import get_object_or_404

# Funciones
# ---------------------------------------------
# TODO: Utils
# ---------------------------------------------
from apps.utils.utils import get_all_icon

# ---------------------------------------------
# TODO: Helpers
# ---------------------------------------------
from apps.utils.helpers import get_content_permisos_detail
from apps.utils.helpers import get_comuna, get_provincia, get_region

# ---------------------------------------------
# TODO: GET MODALES GENERALES
# ---------------------------------------------
def get_modal_icono(request, icon_selected=None):
    iconos = get_all_icon()
    html = render_to_string("partials/_modals/utils/modal_iconos_picker.html", {"iconos": iconos, "icon_selected": icon_selected}, request=request)
    return JsonResponse({"html": html})

def get_modal_direcciones(request, direccion_selected=any):
    # direcciones = get_all_direcciones()
    direcciones = None
    if direccion_selected:
        pass
    html = render_to_string("partials/_models/utils/modal_direcciones", {"direcciones": direcciones }, request=request)
    return JsonResponse({"html": html})

# ---------------------------------------------
# TODO: GET MODALES ESPECIFICOS
# ---------------------------------------------

# ---------------------------------------------
# TODO: Calculos
# ---------------------------------------------

# ---------------------------------------------
# TODO: SIMULADOR
# ---------------------------------------------

# ---------------------------------------------
# TODO: Calculos
# ---------------------------------------------
def select_obtener_ubicacion(request):
    if request.method == "GET":
        try:
            comuna_id = request.GET.get("comuna_id")
            provincia_id = request.GET.get("provincia_id")
            region_numero = request.GET.get("region_numero")

            if comuna_id:
                print("📩 Recibida comuna_id:", comuna_id)
                data = get_comuna(comuna_id)
                print("📤 Respuesta get_comuna:", data)
                return JsonResponse(data)

            if provincia_id:
                print("📩 Recibida provincia_id:", provincia_id)
                data = get_provincia(provincia_id)
                print("📤 Respuesta get_provincia:", data)
                return JsonResponse(data)

            if region_numero:
                print("📩 Recibida region_numero:", region_numero)
                data = get_region(region_numero)
                print("📤 Respuesta get_region:", data)
                return JsonResponse(data)

            return JsonResponse({"error": "No se recibió ningún parámetro válido"}, status=400)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
    return JsonResponse({"error": "Metodo no permitido"}, status=405)

        
# -------------------------------------------------------
# TODO: COMPONENTES
# -------------------------------------------------------
def get_permisos_por_contenttype(request):
    if request.method == "POST":
        content_types = request.POST.getlist("content_types")
        data = get_content_permisos_detail(content_types)
        
        return JsonResponse(data)

    else:
        return JsonResponse({"error": "Metodo no permitido"}, status=405)
