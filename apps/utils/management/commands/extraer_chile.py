import json
from django.core.management.base import BaseCommand
from apps.utils.models import Region, Provincia, Comuna

class Command(BaseCommand):
    help = "Exporta regiones, provincias y comunas en archivos JSON separados"

    def handle(self, *args, **kwargs):
        self.exportar_regiones()
        self.exportar_provincias()
        self.exportar_comunas()
        self.stdout.write(self.style.SUCCESS("→ Archivos JSON generados correctamente"))

    def exportar_regiones(self):
        regiones = Region.objects.all().order_by("numero")
        data = [{"id": r.id, "numero": r.numero, "nombre": r.nombre} for r in regiones]
        with open("regiones.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def exportar_provincias(self):
        provincias = Provincia.objects.all().order_by("id")
        data = [{"id": p.id, "nombre": p.nombre, "nombre_completo":p.nombre_completo, "region_id": p.region.id} for p in provincias]
        with open("provincias.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def exportar_comunas(self):
        comunas = Comuna.objects.all().order_by("id")
        data = [{"id": c.id, "nombre": c.nombre, "provincia_id": c.provincia.id} for c in comunas]
        with open("comunas.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)