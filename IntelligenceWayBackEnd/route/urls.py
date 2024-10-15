from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.CreateRoute.as_view(), name="Crear_ruta"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]