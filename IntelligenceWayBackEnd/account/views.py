from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from preferences.models import ModeloAprendizajeUsuario
from account.models import Medalla



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['user'] = usuario  # Pasar el usuario autenticado al template

        # Obtener el perfil de aprendizaje del usuario
        context['test'] = ModeloAprendizajeUsuario.objects.get(usuario=usuario)

        # Resultados de tests del usuario
        resultados_tests = ModeloAprendizajeUsuario.objects.filter(usuario=usuario)
        context['resultados_tests'] = resultados_tests

        # Obtener las medallas del usuario
        medallas = Medalla.objects.filter(usuario=usuario)
        context['medallas'] = medallas  # Pasar las medallas al contexto

        return context