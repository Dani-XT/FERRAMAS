from django.contrib import admin
from django.utils.html import format_html
from .models import CRUDEntry  

@admin.register(CRUDEntry)
class CRUDEntryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'link_to_crud')

    class Media:
        css = {
            'all': ('admin/custom_admin.css',),
        }

    def link_to_crud(self, obj):
        return format_html('<a class="button" href="/admin/crud/">Acceder a CRUD</a>')

    link_to_crud.short_description = 'Acceso a CRUD'
