from django.db import models
from usuarios.models import Usuario
from categorias.models import Categorias 

class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    monto_fijo = models.FloatField()
    descripcion = models.CharField(max_length=100)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idCategoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre