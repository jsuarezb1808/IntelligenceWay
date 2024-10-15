from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from user.models import User

# Create your models here.


class ModeloAprendizajeUsuario(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    q1 = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    q2 = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    q3 = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    q4 = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    q5 = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    q6 = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    q7 = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    q8 = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)