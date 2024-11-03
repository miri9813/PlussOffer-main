from django.contrib import admin
from .models import Pujas

class AdministrarPujas(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('idPuja', 'fecha_hora', 'monto_final', 'idUsuario')
    search_fields = ('idPuja', 'idUsuario')
    date_hierarchy = 'created'
    list_filter = ('fecha_hora', 'idUsuario')

admin.site.register(Pujas, AdministrarPujas)

# Register your models here.
from .models import Subastas

class SubastasAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')  
    list_display = ('idSubasta', 'MontoInicial', 'FechaHoraInicial', 'FechaHoraFinal', 'IdArticulo')  
    search_fields = ('IdArticulo__nombreArticulo',) 
    list_filter = ('FechaHoraInicial', 'FechaHoraFinal')

admin.site.register(Subastas, SubastasAdmin)