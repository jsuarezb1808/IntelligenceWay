from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from preferences.models import ModeloAprendizajeUsuario

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    
    # Para pasar el contexto al template, puedes sobrescribir el método get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['user'] = usuario  # Pasamos el usuario autenticado al template
        context['test'] = ModeloAprendizajeUsuario.objects.get(usuario=usuario)
        return context