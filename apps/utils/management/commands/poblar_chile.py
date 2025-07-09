import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.utils.models import Region, Provincia, Comuna

class Command(BaseCommand):
    help = 'Puebla la BD desde archivos JSON estáticos de regiones, provincias y comunas'

    def handle(self, *args, **kwargs):
        base_path = os.path.join(settings.BASE_DIR, 'src', 'assets', 'json')

        try:
            with open(os.path.join(base_path, 'regiones.json'), encoding='utf-8') as f:
                regiones = json.load(f)
            with open(os.path.join(base_path, 'provincias.json'), encoding='utf-8') as f:
                provincias = json.load(f)
            with open(os.path.join(base_path, 'comunas.json'), encoding='utf-8') as f:
                comunas = json.load(f)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"❌ Error cargando archivos JSON: {e}"))
            return
        
        # Regiones
        regiones_map = {}
        for r in regiones:
            region, creado = Region.objects.get_or_create(
                numero=r['numero'],
                defaults={'nombre': r['nombre']}
            )
            regiones_map[r['id']] = region
            msg = f"✔ Región: {region.nombre}" if creado else f"⚠️ Región ya existe: {region.nombre}"
            self.stdout.write(self.style.SUCCESS(msg) if creado else self.style.WARNING(msg))

        # Provincias
        provincias_map = {}
        for p in provincias:
            region = regiones_map.get(p['region_id'])
            if not region:
                self.stderr.write(self.style.ERROR(f"❌ Región no encontrada para provincia {p['nombre']}"))
                continue
            provincia, creado = Provincia.objects.get_or_create(
                nombre=p['nombre'],
                region=region,
                defaults={'nombre_completo': p['nombre_completo']}
            )
            provincias_map[p['id']] = provincia
            msg = f"  ↳ Provincia: {provincia.nombre}" if creado else f"  ⚠️ Provincia ya existe: {provincia.nombre}"
            self.stdout.write(self.style.SUCCESS(msg) if creado else self.style.WARNING(msg))

        # Comunas
        for c in comunas:
            provincia = provincias_map.get(c['provincia_id'])
            if not provincia:
                self.stderr.write(self.style.ERROR(f"❌ Provincia no encontrada para comuna {c['nombre']}"))
                continue
            comuna, creado = Comuna.objects.get_or_create(
                nombre=c['nombre'],
                provincia=provincia
            )
            msg = f"     ↳ Comuna: {comuna.nombre}" if creado else f"     ⚠️ Comuna ya existe: {comuna.nombre}"
            self.stdout.write(self.style.SUCCESS(msg) if creado else self.style.WARNING(msg))

        self.stdout.write(self.style.SUCCESS('🎉 ¡Base de datos poblada exitosamente desde archivos JSON!'))
