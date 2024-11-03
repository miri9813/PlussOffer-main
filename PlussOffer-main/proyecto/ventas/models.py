from django.db import models
from usuarios.models import Usuario
from articulos.models import Articulo 
class Pujas(models.Model):
     idPuja = models.AutoField(primary_key=True)  
     fecha_hora = models.DateTimeField(auto_now_add=True)
     monto_final = models.FloatField()
     idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     created = models.DateTimeField(auto_now_add=True) 
     updated = models.DateTimeField(auto_now=True)  

     class Meta:
        verbose_name = "Puja"
        verbose_name_plural = "Pujas"
        ordering = ["fecha_hora"]

     def __str__(self):
        return self.idPuja + ' ' + self.idUsuario

class Subastas(models.Model):
    idSubasta = models.AutoField(primary_key=True, verbose_name="ID Subasta")
    MontoInicial = models.FloatField(verbose_name="Monto Inicial")
    FechaHoraInicial = models.DateTimeField(verbose_name="Fecha y Hora Inicial")
    FechaHoraFinal = models.DateTimeField(verbose_name="Fecha y Hora Final")
    IdArticulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, verbose_name="ID Artículo")
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Subasta"
        verbose_name_plural = "Subastas"
        ordering = ["FechaHoraInicial"]

    def __str__(self):
        return "Subasta " + str(self.idSubasta) + " - " + self.IdArticulo.nombreArticulo