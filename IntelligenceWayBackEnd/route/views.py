from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InteresForm
from .models import Contenido, RutaAprendizaje, Tag
from .algoritmo import EstimacionEstudio
from user.models import User
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

class CreateRoute(View, LoginRequiredMixin):
    template_name = "form.html"
    
    def get(self, request):
        if request.user.is_authenticated:
            form = InteresForm() 
            viewData = {"form": form}
            return render(request, self.template_name, viewData)
        return redirect('login')

    def post(self, request):
        form = InteresForm(data=request.POST)
        viewData = {"form": form}
        
        if form.is_valid():
            # Obtener el interés del formulario
            interes = form.cleaned_data['interes']

            # Obtener los cursos que coinciden con el interés
            cursos = Contenido.objects.filter(tags=interes)

            # Inicializar lista de contenidos válidos
            contenidos_validos = []

            user = request.user
            
            # Filtrar cursos que cumplen con las condiciones
            for curso in cursos:
                if EstimacionEstudio.VerificacionContenido(curso, User.objects.get(id=user.id)) and \
                   EstimacionEstudio.VerificacionTiempo(curso, User.objects.get(id=user.id)):
                    contenidos_validos.append(curso)
            nombreTag = Tag.objects.get(id=interes).tagName
            # Crear la nueva ruta de aprendizaje
            ruta = RutaAprendizaje(
                title=nombreTag,
                description=f"Una rama de contenido enfocado en {nombreTag}",
                usuario=request.user
            )
            ruta.save()

            # Asignar los contenidos a la ruta usando set()
            ruta.contenidos.set(contenidos_validos)
            ruta.save()

            return redirect("profile")
        else:
            return render(request, self.template_name, viewData)


class MyRoutes(ListView):
    model = RutaAprendizaje
    template_name = 'my_routes.html'  # Cambia esto por la ruta a tu plantilla
    context_object_name = 'routes'
    paginate_by = 4  # Número de rutas por página

    def get_queryset(self):
        # Filtrar las rutas del usuario actual
        return RutaAprendizaje.objects.filter(usuario=self.request.user)  # Asegúrate de filtrar según el usuario
    



class RutaDetail(DetailView, LoginRequiredMixin):
    model = RutaAprendizaje
    template_name = 'ruta_detail.html'  # Cambia esto por la ruta a tu plantilla de detalles
    context_object_name = 'route'

class RutaFavoritasView(ListView):
    model = RutaAprendizaje
    template_name = 'ruta_favoritas.html'
    context_object_name = 'rutas_favoritas'

    def get_queryset(self):
        # Filtrar las rutas favoritas del usuario
        return RutaAprendizaje.objects.filter(usuario=self.request.user, favorito=True)

class RutaEliminarView(ListView):
    model = RutaAprendizaje
    template_name = 'ruta_eliminar.html'
    context_object_name = 'rutas'

    def get_queryset(self):
        # Mostrar las rutas del usuario para eliminar
        return RutaAprendizaje.objects.filter(usuario=self.request.user)

class RutaConfirmarEliminarView(View):
    def post(self, request, *args, **kwargs):
        route_id = request.POST.get('route_id')
        ruta = get_object_or_404(RutaAprendizaje, id=route_id, usuario=request.user)
        ruta.delete()
        messages.success(request, 'Ruta eliminada con éxito.')
        return redirect('my_routes')  # Redirigir a la vista de mis rutas