from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, LoginForm
 
# Create your views here.


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('preferencia_update')  # Redirigir a la página de preferencia después del registro

    def form_valid(self, form):
        # Guardar el nuevo usuario
        user = form.save()
        # Iniciar sesión al usuario automáticamente
        login(self.request, user)
        # Redirigir a la página de actualización de preferencias
        return redirect(self.success_url)

class LoginView(View):
    template_name = "login.html"
    
    def get(self, request): 
        if not request.user.is_authenticated:
            form = LoginForm() 
            viewData = {}
            viewData["form"] = form
            return render(request, self.template_name, viewData)
        return redirect('profile')
    
    def post(self, request):
        form = LoginForm(data=request.POST) 
        viewData = {}
        viewData["form"] = form
        if form.is_valid(): 
            login(request, form.get_user()) 
            return redirect('profile')
        else:
            form = LoginForm() 
            return render(request, self.template_name, viewData)
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("index")