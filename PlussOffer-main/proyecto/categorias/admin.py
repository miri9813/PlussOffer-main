from django.contrib import admin
from .models import Categorias

# Register your models here.

class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')  
    list_display = ('idCategoria', 'nombreCategoria')  
    search_fields = ('nombreCategoria',)
    list_filter = ('nombreCategoria',)

admin.site.register(Categorias, CategoriasAdmin)
