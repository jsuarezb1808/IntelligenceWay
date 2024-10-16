from django.urls import path, include
from . import views

urlpatterns = [
    path('update/', views.FormularioView.as_view(), name="preferencia_update"),
    path('calculo-preferencias/', views.CalculoPreferenciasView.as_view(), name='calculo_preferencias'),
]
