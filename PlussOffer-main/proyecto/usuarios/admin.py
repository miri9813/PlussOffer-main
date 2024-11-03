from django.contrib import admin
from .models import Usuario

class AdministrarUsuario(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('idUsuario', 'nombre', 'apellido', 'userName', 'correo', 'celular', 'created', 'updated')
    search_fields = ('idUsuario', 'nombre', 'apellido', 'userName', 'correo')
    date_hierarchy = 'created'
    list_filter = ('idUsuario', 'nombre', 'apellido', 'userName', 'correo', 'celular', 'created')

admin.site.register(Usuario, AdministrarUsuario)

# Register your models here.

