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

class Reporte(models.Model):
    IdContenido = models.ForeignKey(Contenido)
    descripcion = models.TextField(max_length=255)
    
class Favorito(models.Model):
    usuario = models.OneToOneField(User)
    lista = models.ManyToManyField(RutaAprendizaje)
    

'''
class LearningPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='preferences')
    preferred_language = models.CharField(
        max_length=50,
        choices=[('EN', 'English'), ('ES', 'Spanish')],
        default='ES'
    )
    learning_style = models.CharField(
        max_length=50,
        choices=[('video', 'Video'), ('text', 'Text'), ('curso', 'Curso'),('audio','Audio')],
        default='text'
    )

    tipo_interes = models.CharField(
        max_length=10,
        choices=[
            ('python', 'Python'),
            ('java', 'Java'),
            ('django', 'Django'),
        ],
        default='python'
    )

    

    def __str__(self):
        return f"{self.user.username}'s Preferences"


class ContenidoEducacion(models.Model):
    VIDEO = 'video'
    TEXTO = 'texto'
    AUDIO = 'audio'
    PYTHON ='python'
    JAVA= 'java'
    DJANGO ='django'

    
    TIPO_RECURSO_CHOICES = [
        (VIDEO, 'Video'),
        (TEXTO, 'Texto'),
        (AUDIO, 'Audio'),
    ]

    TIPO_DE_INTERES_CHOICES =[
        (PYTHON,'Python'),
        (JAVA, 'Java'),
        (DJANGO,'Django'),

    ]
    
    titulo = models.CharField(max_length=255)
    link = models.URLField()
    descripcion_corta = models.CharField(max_length=500, blank=True)
    tipo_recurso = models.CharField(max_length=5, choices=TIPO_RECURSO_CHOICES, default=VIDEO)
    tipo_interes = models.CharField(max_length=10, choices=TIPO_DE_INTERES_CHOICES, default=PYTHON)
    duracion = models.PositiveIntegerField()  # Duración en un rango de 1 a 3

    
    def __str__(self):
        return self.titulo
    
    def clean(self):
        if not 1 <= self.duracion <= 3:
            raise ValidationError("La duración debe estar entre 1 y 3.")
    
    def obtener_contenidos_por_tipo_interes(cls, tipo_interes):
        return cls.objects.filter(tipo_interes=tipo_interes)
    
    def prueba():
        return print('si funciona')



'''

