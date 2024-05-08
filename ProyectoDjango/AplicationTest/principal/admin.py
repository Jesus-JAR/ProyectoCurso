from django.contrib import admin

# Register your models here.
from models import Tematicas, Autores, Articulos

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido', 'website')
    list_editable = ('nombre','apellido', 'website')
    list_filter = ('apellido')
    search_fields = ['apellido', 'website']
    readonly_fields = ()

# preguntar
admin.site.register(Autores,AutorAdmin)
admin.site.register(Tematicas)
admin.site.register(Articulos)