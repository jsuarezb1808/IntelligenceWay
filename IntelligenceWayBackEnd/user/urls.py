from django.contrib import admin
from django.urls import path
from user import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="registro"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]