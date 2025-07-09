from django.core.management.base import BaseCommand
from apps.utils.utils import get_all_icon
import json
import os

class Command(BaseCommand):
    help = 'Genera un archivo JSON con los iconos del sistema'

    def handle(self, *args, **kwargs):
        iconos = get_all_icon()
        ruta = os.path.join('static', 'data', 'remix_icons.json')
        with open(ruta, 'w', encoding='utf8') as f:
            json.dump(iconos, f, ensure_ascii=False, indent=2)
        self.stdout.write(self.style.SUCCESS(f'se genero correctamente en la ruta {ruta}'))
            