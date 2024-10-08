from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import formularioAprendizajeUsuario
from django.contrib.auth.models import User
# Register your models here.
from .models import ContenidoEducacion, LearningPreferences

@admin.register(ContenidoEducacion)
class ContenidoEducacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_recurso', 'duracion')
    
admin.site.register(formularioAprendizajeUsuario)
admin.site.register(LearningPreferences)