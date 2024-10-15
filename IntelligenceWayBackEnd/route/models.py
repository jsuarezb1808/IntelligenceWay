from django.db import models
from user.models import User
from django.forms import ValidationError

# Create your models here.

class Tag(models.Model):
    tagName = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.tagName}'

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre}'
    
class Contenido(models.Model):
    title = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, default ="Autor borrado", on_delete=models.SET_DEFAULT)
    tags = models.ManyToManyField(Tag, default="Tag borrado")
    duracion =models.IntegerField()
    tipoDeContenido = models.IntegerField()
    link = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    contenidosPrevios = models.ManyToManyField('self', blank=True)
    def __str__(self):
        return f'{self.title}'
    
class RutaAprendizaje(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenidos = models.ManyToManyField(Contenido, related_name='rutas')
    completado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
