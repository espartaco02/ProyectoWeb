from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class Servicio(models.Model):

    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='media/servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo

@receiver(post_delete, sender=Servicio)
def imagen_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.imagen.delete(False)
