from typing import Any
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, UpdateView
from django.views import View
from django import forms
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import rutaAprendizaje, LearningPreferences, ContenidoEducacion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import LearningPreferences
from .models import ContenidoEducacion
from .forms import LearningPreferencesForm
from django.contrib.auth.decorators import login_required
from .algoritmo import EstimacionEstudio
from .forms import AprendizajeForm, LearningPreferencesForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

class IndexView(View):
    template_name = "index.html"
    
    def get(self, request):
        return render(request, self.template_name)

class RegisterView(View):
    template_name = "register.html"
    template_success = "index.html"
    
    def get(self, request): 
        form = UserCreationForm() 
        viewData = {}
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        viewData = {}
        viewData["form"] = form
        if form.is_valid(): 
            login(request, form.save()) 
            return render(request, self.template_success)
        else:
            form = UserCreationForm()
            return render(request, self.template_name, viewData)

class LoginView(View):
    template_name = "login.html"
    template_success = "base.html"
    
    def get(self, request): 
        if not request.user.is_authenticated:
            form = AuthenticationForm() 
            viewData = {}
            viewData["form"] = form
            return render(request, self.template_name, viewData)
        return render(request, self.template_success, viewData)
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST) 
        viewData = {}
        viewData["form"] = form
        if form.is_valid(): 
            login(request, form.get_user()) 
            return render(request, self.template_success)
        else:
            form = AuthenticationForm() 
            return render(request, self.template_name, viewData)
        


def UserLoggedIn(request):
    if request.user.is_authenticated == True:
       username = request.user.username
    else:
      username = None
    return username

class LogoutView(View):
    template_name = "base.html"
    def get(self, request):
        username = UserLoggedIn(request)
        if username != None:
            logout(request)
            return render(request, self.template_name)
        else:
            return render(request, self.template_name)


class FormularioView(View):
    template_name = "form.html"
    template_success = "base.html"
    def get(self, request):
        if request.user.is_authenticated:
            form = AprendizajeForm()
            viewData = {}
            viewData["form"] = form
            viewData["usuario"] = request.user
            return render(request, self.template_name, viewData)
        else:
            return redirect("index")
    
    def post(self, request):
        if request.user.is_authenticated:
            form = AprendizajeForm(request.POST)
            viewData = {}
            viewData["form"] = form
            if form.is_valid(): 
                form.save()
                return render(request, self.template_success)
            else:
                form = AprendizajeForm()
                return render(request, self.template_name, viewData)
        else:
            return redirect("index")
        
class PreferencesUpdateView(UpdateView):
    model = LearningPreferences
    form_class = LearningPreferencesForm
    template_name = 'preferences.html'
    
    # Esto asegura que el formulario siempre se rellene con las preferencias del usuario actual
    def get_object(self, queryset=None):
        # Si las preferencias no existen, las crea
        obj, created = LearningPreferences.objects.get_or_create(user=self.request.user)
        return obj

    # Redirigir después de guardar
    def get_success_url(self):
        return reverse_lazy('index')  # Cambia esto a donde desees redirigir después de guardar
    
@login_required
def iniciar_nueva_ruta(request):
    # Obtenemos el tipo de interés del modelo LearningPreferences del usuario autenticado
    tipo_interes = request.user.preferences.tipo_interes  # 'preferences' es el related_name definido en el modelo

    # Filtra los contenidos que coincidan con el tipo de interés del usuario
    contenidos = ContenidoEducacion.objects.filter(tipo_interes=tipo_interes)[:4]

    # Renderiza la plantilla con los contenidos filtrados
    return render(request, 'ruta_nueva.html', {'contenidos': contenidos})

@login_required
def update_preferences(request):
    if request.method == 'POST':
        form = LearningPreferencesForm(request.POST, instance=request.user.preferences)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige al perfil o a donde prefieras
    else:
        form = LearningPreferencesForm(instance=request.user.preferences)

    return render(request, 'update_preferences.html', {'form': form})