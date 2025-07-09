from django import forms
from django.contrib.auth.models import Group, Permission
from apps.access.roles.models import DescripcionGrupo

class AddUpdateGrupoForm(forms.Form):
    nombre = forms.CharField(max_length=150)
    descripcion = forms.CharField(widget=forms.Textarea)
    bg_color = forms.CharField(max_length=150, required=False)
    icono = forms.CharField(max_length=150, required=False)
    permisos = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(), required=True)
    

    def __init__(self, *args, instance=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = instance

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        qs = Group.objects.filter(name__iexact=nombre)
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("El nombre del grupo ya existe")

        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data["descripcion"]

        return descripcion
    
    def save(self):
        data = self.cleaned_data
        if self.instance:
            self.instance.name = data["nombre"]
            self.instance.save()

            desc_grupo = self.instance.descripcion
            desc_grupo.descripcion = data["descripcion"]
            desc_grupo.bg_color = data["bg_color"]
            desc_grupo.icono = data["icono"]
            desc_grupo.save()

            self.instance.permissions.set(data["permisos"])
            return self.instance
        else:
            grupo = Group.objects.create(
                name=data["nombre"]
            )
            desc_grupo = DescripcionGrupo.objects.create(
                grupo=grupo,
                descripcion=data["descripcion"],
                bg_color=data["bg_color"],
                icono=data["icono"]
            )
            grupo.permissions.set(data["permisos"])
            return grupo

  
