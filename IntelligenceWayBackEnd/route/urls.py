from django.urls import path, include
from . import views





urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('', include('social_django.urls')),
    path('survey/', views.LearningMethods,name='survey'),
]

