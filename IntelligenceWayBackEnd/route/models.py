from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.forms import ValidationError

# Create your models here.

class rutaAprendizaje(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class formularioAprendizajeUsuario(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    q1 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    q2 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    q3 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    q4 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    q5 = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    q6 = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    q7 = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    q8 = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)



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
        """
        Obtiene todos los contenidos cuyo tipo de interés coincida con el valor dado.
        
        :param tipo_interes: El tipo de interés que deseas filtrar (e.g., 'django', 'python', 'java')
        :return: QuerySet con todos los objetos ContenidoEducacion que coincidan con el tipo de interés
        """
        return cls.objects.filter(tipo_interes=tipo_interes)
    
    def prueba():
        return print('si funciona')






