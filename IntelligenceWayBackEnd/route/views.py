from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InteresForm
from .models import Contenido, RutaAprendizaje, Tag
from .algoritmo import VerificacionContenido,VerificacionTiempo
from user.models import User
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic.edit import FormMixin
from .forms import ReporteForm
from django.urls import reverse





class ContenidoDetailView(FormMixin, DetailView):
    model = Contenido
    template_name = 'contenido_detail.html'
    context_object_name = 'contenido'
    form_class = ReporteForm

    def get_success_url(self):
        # Redirigir a la misma página después de enviar el reporte
        return reverse('contenido_detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            # Crear el reporte
            reporte = form.save(commit=False)
            reporte.IdContenido = self.object
            reporte.save()
            messages.success(request, '¡Reporte enviado exitosamente!')  # Mensaje de éxito
            return self.form_valid(form)
        else:
            messages.error(request, 'Hubo un error al enviar el reporte. Inténtalo de nuevo.')  # Mensaje de error
            return self.form_invalid(form)




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
                if VerificacionContenido(curso, User.objects.get(id=user.id)) and \
                   VerificacionTiempo(curso, User.objects.get(id=user.id)):
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
    



class RutaDetail(LoginRequiredMixin, DetailView):
    model = RutaAprendizaje
    template_name = 'ruta_detail.html'  # Asegúrate de que esta es la ruta a tu plantilla de detalles
    context_object_name = 'route'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar los contenidos de la ruta al contexto
        context['contenidos'] = self.object.contenidos.all()
        return context

class RutaFavoritasView(ListView):
    model = RutaAprendizaje
    template_name = 'ruta_favoritas.html'
    context_object_name = 'rutas_favoritas'

    def get_queryset(self):
        # Supongamos que tienes un método para obtener las rutas favoritas del usuario
        return RutaAprendizaje.objects.filter(favorito=True, usuario=self.request.user)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, 4)  # Muestra 4 rutas por página
        page_number = request.GET.get('page')
        rutas_favoritas = paginator.get_page(page_number)
        return render(request, self.template_name, {'rutas_favoritas': rutas_favoritas})
    
#-----------------------------------------------------------

class RouteDeleteFavorite(ListView):
    model=RutaAprendizaje
    template_name='favoritos_eliminar.html'
    
    def get_queryset(self):
        return RutaAprendizaje.objects.filter(favorito=True, usuario=self.request.user)
    
class RouteConfirmDeleteFavorite(View):
    def post(self,request,*args,**kwargs):
        favorite_id=request.POST.get('favorite_id')
        favorite=get_object_or_404(RutaAprendizaje, id=favorite_id, usuario=self.request.user)
        favorite.delete()
        messages.success(request,'ruta fue eliminada de favoritos con exito')
        return redirect('my_routes')  # Redirigir a la vista de mis rutas
#-----------------------------------------------------------

class RutaEliminarView(ListView):
    model = RutaAprendizaje
    template_name = 'ruta_eliminar.html'
    context_object_name = 'rutas'
    paginate_by = 4

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