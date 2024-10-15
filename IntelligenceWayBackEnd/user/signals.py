from django.db.models.signals import post_save
from django.dispatch import receiver
from preferences.models import ModeloAprendizajeUsuario
from .models import User

@receiver(post_save, sender=User)
def crear_modelo_automáticamente(sender, instance, created, **kwargs):
    if created:
        # Se crea un carrito asociado al usuario si el usuario ha sido creado
        ModeloAprendizajeUsuario.objects.create(usuario=instance)