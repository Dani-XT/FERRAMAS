from django import forms

class MultipleImageInput(forms.ClearableFileInput):
    allow_multiple_selected = True

    def __init__(self, attrs=None):
        final_attrs = {'multiple': True}
        if attrs:
            final_attrs.update(attrs)
        super().__init__(attrs=final_attrs)

class MultipleImageField(forms.ImageField):
    widget = MultipleImageInput

    def clean(self, data, initial=None):
        if not data and initial:
            return initial
        
        single_image_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_image_clean(d, initial) for d in data]
        
        return [single_image_clean(data, initial)]