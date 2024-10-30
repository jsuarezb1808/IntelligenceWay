from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from preferences.models import ModeloAprendizajeUsuario

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    
    # To pass the context to the template, you can override the get_context_data method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context['user'] = usuario  # Pass the authenticated user to the template
        context['test'] = ModeloAprendizajeUsuario.objects.get(usuario=usuario)
        return context
