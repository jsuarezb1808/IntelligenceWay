from django.urls import path
from home import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutUsView.as_view(), name='about_us'),

]