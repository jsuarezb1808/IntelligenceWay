from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

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