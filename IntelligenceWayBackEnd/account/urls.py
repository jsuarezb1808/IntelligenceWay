from django.urls import path, include
from account import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile' )
]
