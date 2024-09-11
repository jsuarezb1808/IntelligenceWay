from typing import Any
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views import View
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from .models import rutaAprendizaje
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import LearningPreferences
from .forms import LearningPreferencesForm
# Create your views here.

class IndexView(View):
    template_name = "base.html"
    
    def get(self, request):
        return render(request, self.template_name)

class RegisterView(View):
    template_name = "register.html"
    template_success = "base.html"
    
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
        form = AuthenticationForm() 
        viewData = {}
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST) 
        viewData = {}
        viewData["form"] = form
        if form.is_valid(): 
            print("wtf")
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