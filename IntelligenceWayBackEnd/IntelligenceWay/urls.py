"""IntelligenceWay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''
from django.contrib import admin
from django.urls import path
from route.views import RegisterView, LoginView, LogoutView, IndexView,PreferencesUpdateView,iniciar_nueva_ruta,update_preferences,FormularioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name="registro"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('formulario/', FormularioView.as_view(), name='formulario' ),
    path('preferences/', PreferencesUpdateView.as_view(), name='update_preferences'),
    path('iniciar-nueva-ruta/', iniciar_nueva_ruta, name='iniciar_nueva_ruta'),
]
'''

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')),

    
    path('user/', include('user.urls')),
    path('account/', include('account.urls')),
    path('route/', include('route.urls')),
    path('preferences/', include('preferences.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)