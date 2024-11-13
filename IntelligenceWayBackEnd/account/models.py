from django.db import models
from user.models import User
from route.models import RutaAprendizaje

class Medalla(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medallas')
    ruta = models.ForeignKey(RutaAprendizaje, on_delete=models.CASCADE)
    fecha_otorgada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medalla para {self.usuario.email} - {self.ruta.title}"
