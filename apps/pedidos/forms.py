from django import forms

class PedidoAddUpdateForm(forms.Form):
    numero_pedido = forms.CharField(max_length=150)