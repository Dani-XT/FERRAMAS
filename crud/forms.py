from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from django import forms
from apps.front.home.models import Producto, Editorial, Tipo

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        # Solo establece la contraseña si se proporciona una
        if self.cleaned_data["password"]:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    

#PRODUCTOS
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'imagen', 'precio', 'stock', 'editorial', 'tipo']



class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre', 'descripcion']
        
#TIPO



class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['nombre', 'descripcion']
