from django import forms
from django.contrib.auth.models import Group, User
from django.utils.crypto import get_random_string

class UsuarioAddUpdateForm(forms.Form):
    username = forms.CharField(max_length=150)
    nombre = forms.CharField(max_length=150)
    apellido = forms.CharField(max_length=150)
    email = forms.EmailField()
    grupo = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.generated_password = get_random_string(10)
        self.instance = instance

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if self.instance:
            if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
                raise forms.ValidationError("Este username ya se encuentra en uso")
        else:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("Este username ya se encuentra en uso")
        return username

    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if self.instance:
            if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
                raise forms.ValidationError("Este correo ya está registrado.")
        else:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Este correo ya está registrado.")
        return email

    def save(self):
        data = self.cleaned_data

        if self.instance:
            usuario = self.instance
            usuario.username = data["username"]
            usuario.email = data["email"]
            usuario.first_name = data["nombre"]
            usuario.last_name = data["apellido"]
            usuario.groups.set([data["grupo"]])
            usuario.save()
            return usuario, None  # 👈 Devuelve tupla siempre (coherente con creación)
        else:
            usuario = User.objects.create_user(
                username=data["username"],
                email=data["email"],
                password=self.generated_password,
                first_name=data["nombre"],
                last_name=data["apellido"],
            )
            usuario.groups.set([data["grupo"]])
            return usuario, self.generated_password