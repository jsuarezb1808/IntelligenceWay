from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import AprendizajeForm
from django.views import View
from django.views.generic.edit import UpdateView
from .models import ModeloAprendizajeUsuario
from route.algoritmo import PreferenciasContenido,PreferenciasTiempo
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

# Create your views here.
class FormularioView(LoginRequiredMixin, UpdateView):
    model = ModeloAprendizajeUsuario
    form_class = AprendizajeForm
    template_name = 'test.html'
    success_url = reverse_lazy('calculo_preferencias')
    
    def get_object(self):
        return ModeloAprendizajeUsuario.objects.get(usuario=self.request.user)
    


class CalculoPreferenciasView(TemplateView):
    template_name = 'calculo_preferencias.html'  # Cambia el nombre según tu estructura

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el objeto asociado al usuario actual
        usuario = self.request.user
        modelo_usuario = get_object_or_404(ModeloAprendizajeUsuario, usuario=usuario)

        # Realizar los cálculos
        preferencias_contenido = PreferenciasContenido(modelo_usuario)
        preferencias_tiempo = PreferenciasTiempo(modelo_usuario)
        
        # Guardar los valores en el modelo User
        usuario.preferenciaAudio = preferencias_contenido[1]  # Audio
        usuario.preferenciaVideo = preferencias_contenido[2]  # Video
        usuario.preferenciaTexto = preferencias_contenido[0]   # Texto
        usuario.tiempoAprendizaje = preferencias_tiempo     # Tiempo de aprendizaje
        usuario.save()  # Guardar cambios en el usuario

        # Pasar los resultados al contexto
        context['preferencias_contenido'] = preferencias_contenido
        context['preferencias_tiempo'] = preferencias_tiempo

        return context


       