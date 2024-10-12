from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import formularioAprendizajeUsuario, ContenidoEducacion, CustomUser

# Register your models here.
@admin.register(ContenidoEducacion)
class ContenidoEducacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_recurso', 'duracion')

admin.site.register(formularioAprendizajeUsuario)


admin.site.unregister(CustomUser) 
admin.site.register(CustomUser, UserAdmin) 