from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Manager para el modelo User
class MyUserManager(BaseUserManager):
    def create_user(self, email, nombre, apellido, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')

        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, apellido=apellido)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, apellido, password=None):
        user = self.create_user(email, nombre, apellido, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Modelo de usuario personalizado
class User(AbstractBaseUser, PermissionsMixin):
    ROLES = [
        ('admin', 'Admin'),
        ('usuario', 'Usuario')
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tiempo = models.IntegerField(default=1)
    content = models.FloatField(default=1)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    preferenciaAudio=models.IntegerField(null=True)
    preferenciaVideo=models.IntegerField(null=True)
    preferenciaTexto=models.IntegerField(null=True)
    tiempoAprendizaje=models.IntegerField(null=True)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return self.email
