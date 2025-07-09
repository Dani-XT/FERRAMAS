from django import forms

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from apps.access.permisos.models import DescripcionPermiso, DescripcionContent


class AddUpdateModeloForm(forms.Form):
    model = forms.CharField(max_length=100)
    app_label = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    icono = forms.CharField(max_length=150, required=False)
    bg_color = forms.CharField(max_length=150, required=False)

    def __init__(self, *args, instance=None, **kwargs):    
        super().__init__(*args, **kwargs)
        self.instance = instance

    def clean_model(self):
        pass

    def clean_descripcion(self):
        descripcion = self.cleaned_data["descripcion"]
        return descripcion.capitalize()

    def save(self):
        data = self.cleaned_data
        if self.instance:
            content = self.instance.content
            content.app_label = data["app_label"]
            content.model = data["model"]

            self.instance.descripcion = data["descripcion"]
            self.instance.bg_color = data["bg_color"]
            self.instance.icono = data["icono"]

            content.save()
            self.instance.save()

            return self.instance

        content = ContentType.objects.create(
            app_label = data["app_label"],
            model = data["model"]
        )

        desc_content = DescripcionContent.objects.create(
            content = content,
            descripcion = data["descripcion"],
            bg_color = data["bg_color"],
            icono = data["icono"],
        )



    
    