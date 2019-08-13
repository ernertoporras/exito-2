from django.db import models

# Create your models here.

class Personal(models.Model):
    nombre =models.CharField(max_length=200, verbose_name="Nombre")
    telefono=models.CharField(max_length=10 , verbose_name="Telefono")
    direccion=models.TextField(verbose_name="Direccion")

    class Meta:
        verbose_name="Personal"
        verbose_name_plural="Personales"

    def __str__(self):
        return self.nombre