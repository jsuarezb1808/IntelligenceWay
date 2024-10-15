from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.CreateRoute.as_view(), name="Crear_ruta"),
]