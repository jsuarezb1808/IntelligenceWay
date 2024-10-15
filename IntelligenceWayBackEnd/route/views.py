from django.views import View
from django import forms
from django.shortcuts import render,redirect
from django.views import View

from .models import Contenido,RutasdeAprendizaje

#recibe que le interesa aprender al usuario y crea la ruta
class CrearRuta():
    template_name='form.html'
    def post(self,request):
        form = LoginForm(data=request.POST) 
        viewData = {}
        viewData["form"] = form
        if form.is_valid(): 
            pass
        else:
            form = LoginForm() 
            return render(request, self.template_name, viewData)

         

#Read
def VerRuta():
    pass

#Update
def actualizarRuta():
    pass
#remove
def RemoverRuta():
    pass