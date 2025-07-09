from django.core.management.base import BaseCommand
from django.core.management import call_command

# Modelos
from apps.utils.models import GrupoValor, ValorSistema
from auth.models import (
    SituacionPrevisional,
    CondicionHabitacional,
    PostulacionesPrevias,
    Sexo,
    NivelEducacional
)

class Command(BaseCommand):
    help = "Genera las tablas y relaciones básicas del sistema"

    def handle(self, *args, **kwargs):
        self.poblar_grupo_tiempo()
        self.poblar_modelos_usuario()
        self.ejecutar_poblar_chile()

    def poblar_grupo_tiempo(self):
        grupo_nombre = "tiempo"
        valores = [
            ("día", "Unidad de tiempo en singular"),
            ("días", "Unidad de tiempo en plural"),
            ("semana", "Unidad de tiempo en singular"),
            ("semanas", "Unidad de tiempo en plural"),
            ("mes", "Unidad de tiempo en singular"),
            ("meses", "Unidad de tiempo en plural"),
            ("año", "Unidad de tiempo en singular"),
            ("años", "Unidad de tiempo en plural"),
        ]

        grupo, creado = GrupoValor.objects.get_or_create(
            nombre=grupo_nombre,
            defaults={'descripcion': "Unidades de tiempo para uso del Sistema"}
        )

        if creado:
            self.stdout.write(self.style.SUCCESS(f'Grupo "{grupo_nombre}" creado.'))
        else:
            self.stdout.write(self.style.WARNING(f'Grupo "{grupo_nombre}" ya existe.'))

        for clave, descripcion in valores:
            valor, creado = ValorSistema.objects.get_or_create(
                clave=clave,
                grupo=grupo,
                defaults={'valor': clave, 'descripcion': descripcion}
            )
            msg = f'  → Valor "{clave}" {"creado" if creado else "ya existe"}'
            self.stdout.write(self.style.SUCCESS(msg) if creado else self.style.WARNING(msg))

    def poblar_modelos_usuario(self):
        datos = {
            SituacionPrevisional: [
                ("AFP", "Cotiza en AFP"),
                ("Independiente", "Independiente"),
                ("Informal", "Trabajo Informal"),
                ("Cesante", "Cesante"),
            ],
            CondicionHabitacional: [
                ("Allegado", "Allegado"),
                ("Arrendatario", "Arrendatario"),
                ("Propietario", "Propietario"),
                ("Otro", "Otro"),
            ],
            PostulacionesPrevias: [
                ("Ninguna", "No ha postulado anteriormente"),
                ("Anterior con rechazo", "Postulación rechazada"),
                ("Anterior con éxito", "Postulación exitosa"),
            ],
            Sexo: [
                ("Femenino", "Mujer"),
                ("Masculino", "Hombre"),
                ("Otro", "Prefiere no decir"),
            ],
            NivelEducacional: [
                ("Básica", "Educación Básica"),
                ("Media", "Educación Media"),
                ("Técnico", "Técnico Profesional"),
                ("Universitaria", "Universitaria o superior"),
            ],
        }

        for modelo, valores in datos.items():
            for nombre, descripcion in valores:
                obj, creado = modelo.objects.get_or_create(
                    nombre=nombre,
                    defaults={"descripcion": descripcion}
                )
                msg = f'{modelo.__name__} "{nombre}" {"creado" if creado else "ya existe"}'
                self.stdout.write(self.style.SUCCESS(f'✔️ {msg}') if creado else self.style.WARNING(f'⚠️ {msg}'))

    def ejecutar_poblar_chile(self):
        try:
            call_command("poblar_chile")
            self.stdout.write(self.style.SUCCESS("✔️ Comando poblar_chile ejecutado correctamente."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Error al ejecutar poblar_chile: {e}'))
