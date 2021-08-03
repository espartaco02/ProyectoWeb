from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class CategoriaProd(models.Model):

    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoriaProd'
        verbose_name_plural='categoriasProd'

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=7, decimal_places=2) 
    imagen = models.ImageField(upload_to='media/tienda', null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre

@receiver(post_delete, sender=Producto)
def imagen_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.imagen.delete(False)

