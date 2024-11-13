from django.db import models
from user.models import User
from django.forms import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

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
    
    NIVEL_DIFICULTAD = [
        (1, 'Introductorio'),
        (2, 'Principiante-Básico'),
        (3, 'Principiante-Intermedio'),
        (4, 'Intermedio'),
        (5, 'Intermedio-Avanzado'),
        (6, 'Avanzado'),
        (7, 'Muy Avanzado'),
        (8, 'Experto'),
    ]
    
    title = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, default="Autor borrado", on_delete=models.SET_DEFAULT)
    tags = models.ManyToManyField(Tag, default="Tag borrado")
    duracion = models.IntegerField()
    tipoDeContenido = models.IntegerField()
    link = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    nivel = models.IntegerField(choices=NIVEL_DIFICULTAD)
    contenidosPrevios = models.ManyToManyField('self', blank=True)
    imagen = models.ImageField(
        upload_to='IntelligenceWay/static/contenidos/img/', 
        null=True, blank=True, 
    )

    def __str__(self):
        return f'{self.title} - {self.id}'
    
class RutaAprendizaje(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenidos = models.ManyToManyField(Contenido, through='ProgresoContenido', related_name='rutas')
    completado = models.BooleanField(default=False)
    
    def get_completado_percentage(self):
        total_contenidos = self.contenidos.count()
        contenidos_completados = self.contenidos.filter(progresocontenido__completado=True).count()
        if total_contenidos == 0:
            return 0
        return (contenidos_completados / total_contenidos) * 100
    
    def __str__(self):
        return self.title


class ProgresoContenido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    ruta = models.ForeignKey(RutaAprendizaje, on_delete=models.CASCADE)
    completado = models.BooleanField(default=False)
    fecha_completado = models.DateTimeField(null=True, blank=True)
    calificacion = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True
    )

    def save(self, *args, **kwargs):
        # Guardamos el estado actual del campo completado antes de cambiarlo
        estado_anterior = None
        if self.pk:
            estado_anterior = ProgresoContenido.objects.get(pk=self.pk).completado

        # Si el contenido se marca como completado y antes no estaba completado
        if self.completado and estado_anterior is not True:
            self.fecha_completado = self.fecha_completado or timezone.now()
            ProgresoContenido.objects.filter(
                usuario=self.usuario,
                contenido=self.contenido
            ).update(completado=True, fecha_completado=self.fecha_completado)

        # Si el contenido se desmarca como completado y antes estaba completado
        elif not self.completado and estado_anterior is True:
            ProgresoContenido.objects.filter(
                usuario=self.usuario,
                contenido=self.contenido
            ).update(completado=False, fecha_completado=None)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.contenido.title} - {'Completado' if self.completado else 'En progreso'}"


class Reporte(models.Model):
    ERROR_CHOICES = [
        ('gramatica_ortografia', 'Error de gramática o ortografía'),
        ('enlace_roto', 'Enlace roto'),
        ('error_formato', 'Error de formato'),
        ('imagen_video_no_visible', 'Imágenes o videos no visibles'),
        ('contenido_incorrecto', 'Error en el contenido'),
        ('problemas_audio', 'Problemas de audio'),
        ('problema_navegacion', 'Problema de navegación'),
        ('contenido_no_accesible', 'Contenido no accesible'),
        ('error_ejercicio', 'Error en ejercicios o cuestionarios'),
        ('tiempo_carga', 'Tiempo de carga lento'),
        ('compatibilidad', 'Problemas de compatibilidad'),
        ('error_traduccion', 'Error de traducción'),
    ]

    idContenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50, choices=ERROR_CHOICES)

    def __str__(self):
        return f"{self.idContenido.title} - {self.get_descripcion_display()}"

    
class Favorito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    lista = models.ManyToManyField(RutaAprendizaje, blank=True)
    def __str__(self):
        return self.usuario.email


