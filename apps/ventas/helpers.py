from apps.ventas.models import Venta

def get_all_ventas():
    return Venta.objects.all().order_by('id')