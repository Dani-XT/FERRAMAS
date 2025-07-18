from apps.pedidos.models import Pedido


def get_all_pedidos():
    return Pedido.objects.all().order_by('id')