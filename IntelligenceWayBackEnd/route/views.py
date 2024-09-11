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
    
    