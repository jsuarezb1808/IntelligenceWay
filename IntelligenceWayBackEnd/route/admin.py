from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *
# Register your models here.

admin.site.register(Tag)
admin.site.register(Autor)
admin.site.register(Contenido)
admin.site.register(RutaAprendizaje)