from django import forms
from django.core.validators import MinValueValidator, MaxLengthValidator

# Modelos
from apps.productos.models import Producto, Status, ImagenProducto
from apps.utils.forms import MultipleImageField, MultipleImageInput

# Contrib
from apps.utils.utils import limpiar_numeros_entero

class ProductoAddUpdateForm(forms.Form):
    nombre = forms.CharField(max_length=150)
    alias = forms.CharField(max_length=150)
    descripcion = forms.CharField(widget=forms.Textarea)
    precio = forms.CharField(max_length=150)
    stock = forms.BooleanField(required=False)
    cantidad = forms.IntegerField(validators=[MinValueValidator(0)])
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    # imagenes = MultipleImageField(required=True)

    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = instance
        
        print(kwargs.get("files",None))

        # if not self.instance:
        #     self.fields['imagenes'].required = True
    
    def clean_precio(self):
        precio = self.cleaned_data["precio"]
        print("antes",precio)
        precio = limpiar_numeros_entero(precio)
        print(precio)

        return precio


    def save(self):
        data = self.cleaned_data
        if self.instance:
            producto = self.instance
            producto.nombre = data["nombre"]
            producto.alias = data["alias"]
            producto.descripcion = data["descripcion"]
            producto.precio = data["precio"]
            producto.stock = data["stock"]
            producto.cantidad = data["cantidad"]
            producto.status = data["status"]

        else:
            producto = Producto.objects.create(
                nombre = data["nombre"],
                alias = data["alias"],
                descripcion = data["descripcion"],
                precio = data["precio"],
                stock = data["stock"],
                cantidad = data["cantidad"],
                status = data["status"]
            )

        for imagen in self.files.getlist('imagenes'):
            imagen = ImagenProducto.objects.create(producto = producto, imagen = imagen)

        return producto
            


        
