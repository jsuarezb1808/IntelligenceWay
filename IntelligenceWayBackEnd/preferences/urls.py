from django.urls import path, include
from . import views

urlpatterns = [
    path('update/', views.FormularioView.as_view(), name="preferencia-update"),
]
