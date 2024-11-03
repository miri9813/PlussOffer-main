from django.db import models

class Categorias(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name="ID CATEGORIA")
    nombreCategoria = models.CharField(max_length=100, verbose_name="Nombre de la categoria")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["created"]

    def __str__(self):
        return self.nombreCategoria

# Create your models here.
