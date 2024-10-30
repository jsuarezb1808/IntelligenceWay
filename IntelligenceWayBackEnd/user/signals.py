from django.db.models.signals import post_save
from django.dispatch import receiver
from preferences.models import ModeloAprendizajeUsuario
from .models import User
from route.models import Favorito

@receiver(post_save, sender=User)
def crear_modelo_automáticamente(sender, instance, created, **kwargs):
    if created:
        ModeloAprendizajeUsuario.objects.create(usuario=instance)
        Favorito.objects.create(usuario=instance)