from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import AprendizajeForm
from django.views import View
from django.views.generic.edit import UpdateView
from .models import ModeloAprendizajeUsuario
# Create your views here.
class FormularioView(LoginRequiredMixin, UpdateView):
    model = ModeloAprendizajeUsuario
    form_class = AprendizajeForm
    template_name = 'test.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        return ModeloAprendizajeUsuario.objects.get(usuario=self.request.user)