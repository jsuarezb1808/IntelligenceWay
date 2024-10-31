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
    autor = models.ForeignKey(Autor, default="Autor borrado", on_delete=models.SET_DEFAULT)
    tags = models.ManyToManyField(Tag, default="Tag borrado")
    duracion = models.IntegerField()
    tipoDeContenido = models.IntegerField()
    link = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    contenidosPrevios = models.ManyToManyField('self', blank=True)
    imagen = models.ImageField(
        upload_to='IntelligenceWay/static/contenidos/img/', 
        null=True, blank=True, 
        default='IntelligenceWay/static/contenidos/img/default_image.jpg'
    )

    def __str__(self):
        return f'{self.title}'
    
class RutaAprendizaje(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenidos = models.ManyToManyField(Contenido, through='ProgresoContenido', related_name='rutas')
    completado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class ProgresoContenido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    ruta = models.ForeignKey(RutaAprendizaje, on_delete=models.CASCADE)
    completado = models.BooleanField(default=False)
    fecha_completado = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.contenido.title} - {'Completado' if self.completado else 'En progreso'}"

class Reporte(models.Model):
    idContenido = models.ForeignKey(Contenido, default="Usuario borrado", on_delete=models.SET_DEFAULT)
    descripcion = models.TextField(max_length=255)
    def __str__(self):
        return self.idContenido.title
    
class Favorito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    lista = models.ManyToManyField(RutaAprendizaje, blank=True)
    def __str__(self):
        return self.usuario.email


