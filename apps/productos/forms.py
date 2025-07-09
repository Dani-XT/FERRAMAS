from django import forms

class ProductoAddUpdateForm(forms.Form):
    nombre = forms.CharField(max_length=150)
    alias = forms.CharField(max_length=150)
    