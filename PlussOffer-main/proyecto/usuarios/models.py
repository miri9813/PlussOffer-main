from django.db import models
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name="ID Usuario")
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    apellido = models.CharField(max_length=200, verbose_name="Apellido")
    userName = models.CharField(max_length=200, verbose_name="Username")
    celular = models.CharField(max_length=15, verbose_name="Celular")  
    correo = models.EmailField(max_length=254, verbose_name="Correo Electrónico")  
    contraseña = models.CharField(max_length=128, verbose_name="Contraseña") 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["created"]

    def __str__(self):
        return self.nombre + ' ' + self.apellido

# Create your models here.
