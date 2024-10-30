from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import AprendizajeForm
from django.views import View
from django.views.generic.edit import UpdateView
from .models import ModeloAprendizajeUsuario
from route.algoritmo import PreferenciasContenido, PreferenciasTiempo
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
    template_name = 'calculo_preferencias.html'  # Change the name according to your structure

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the object associated with the current user
        usuario = self.request.user
        modelo_usuario = get_object_or_404(ModeloAprendizajeUsuario, usuario=usuario)

        # Perform calculations
        preferencias_contenido = PreferenciasContenido(modelo_usuario)
        preferencias_tiempo = PreferenciasTiempo(modelo_usuario)
        
        # Save the values in the User model
        usuario.preferenciaAudio = preferencias_contenido[1]  # Audio
        usuario.preferenciaVideo = preferencias_contenido[2]  # Video
        usuario.preferenciaTexto = preferencias_contenido[0]   # Text
        usuario.tiempoAprendizaje = preferencias_tiempo     # Learning time
        usuario.save()  # Save changes to the user

        # Pass the results to the context
        context['preferencias_contenido'] = preferencias_contenido
        context['preferencias_tiempo'] = preferencias_tiempo

        return context
