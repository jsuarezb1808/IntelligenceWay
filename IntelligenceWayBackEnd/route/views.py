from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InteresForm
from .models import Contenido, RutaAprendizaje, Tag, Favorito, ProgresoContenido
from .algoritmo import VerificacionContenido, VerificacionTiempo
from user.models import User
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic.edit import FormMixin
from .forms import ReporteForm
from django.urls import reverse
from django.utils import timezone

class ContenidoDetailView(FormMixin, DetailView):
    model = Contenido
    template_name = 'contenido_detail.html'
    context_object_name = 'contenido'
    form_class = ReporteForm

    def get_success_url(self):
        # Redirect to the same page after submitting the report
        return reverse('contenido_detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            # Create the report
            reporte = form.save(commit=False)
            reporte.idContenido = self.object
            reporte.save()
            messages.success(request, 'Reporte enviado exitosamente.')  # Success message
            return self.form_valid(form)
        else:
            messages.error(request, 'Hubo un error en el envío del reporte. Intenta de nuevo.')  # Error message
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
            # Obtén el interés del formulario
            interes = form.cleaned_data['interes']

            # Obtén los cursos que coinciden con el interés
            cursos = Contenido.objects.filter(tags=interes)

            # Inicializa la lista de contenidos válidos
            contenidos_validos = []

            user = request.user
            
            # Filtra los cursos que cumplen con las condiciones
            for curso in cursos:
                if VerificacionContenido(curso, User.objects.get(id=user.id)) and \
                   VerificacionTiempo(curso, User.objects.get(id=user.id)):
                    contenidos_validos.append(curso)
            
            nombreTag = Tag.objects.get(id=interes).tagName

            # Crea la nueva ruta de aprendizaje
            ruta = RutaAprendizaje(
                title=nombreTag,
                description=f"Una ruta enfocada en conocimientos relacionados a {nombreTag}",
                usuario=user
            )
            ruta.save()

            # Asocia manualmente cada contenido con la ruta de aprendizaje mediante ProgresoContenido
            for contenido in contenidos_validos:
                ProgresoContenido.objects.create(
                    usuario=user,
                    ruta=ruta,
                    contenido=contenido,
                    completado=False
                )

            return redirect("my_routes")
        else:
            return render(request, self.template_name, viewData)
class MyRoutes(ListView):
    model = RutaAprendizaje
    template_name = 'my_routes.html'  # Cambia esto al nombre correcto de tu template
    context_object_name = 'routes'
    paginate_by = 4  # Número de rutas por página

    def get_queryset(self):
        # Filtra las rutas del usuario actual
        return RutaAprendizaje.objects.filter(usuario=self.request.user)  # Asegúrate de filtrar por el usuario

    def get_context_data(self, **kwargs):
        # Obtén el contexto base
        context = super().get_context_data(**kwargs)
        
        # Calcula el porcentaje completado para cada ruta
        for route in context['routes']:
            # Contar los contenidos totales y completados en la ruta
            total_contenidos = route.contenidos.count()
            contenidos_completados = route.progresocontenido_set.filter(completado=True).count()
            
            # Si hay contenidos, calcular el porcentaje de completado
            if total_contenidos > 0:
                porcentaje_completado = (contenidos_completados / total_contenidos) * 100
            else:
                porcentaje_completado = 0  # Si no hay contenidos, el progreso es 0

            # Añadir el porcentaje calculado al contexto
            route.porcentaje_completado = porcentaje_completado

        return context


class RutaDetail(LoginRequiredMixin, DetailView):
    model = RutaAprendizaje
    template_name = 'ruta_detail.html'
    context_object_name = 'route'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar los contenidos de la ruta al contexto
        context['contenidos'] = self.object.contenidos.all()
        
        # Crear un diccionario para el progreso
        progreso_dict = {}
        for contenido in context['contenidos']:
            # Verifica si hay un progreso registrado para el contenido del usuario actual
            progreso = ProgresoContenido.objects.filter(usuario=self.request.user, contenido=contenido).first()
            if progreso:
                progreso_dict[contenido.id] = progreso.completado  # Solo guarda el estado de completado
            else:
                progreso_dict[contenido.id] = False  # Si no hay progreso, se considera no completado
        
        context['progreso_dict'] = progreso_dict

        # Verificar si el usuario tiene un favorito
        favorito = Favorito.objects.filter(usuario=self.request.user).first()
        idRuta = self.get_object().id
        ruta_actual = RutaAprendizaje.objects.get(id=idRuta)
        if ruta_actual in favorito.lista.all():
            # Verificar si el contenido está en los favoritos
            contenido_en_favoritos = True
        else:
            contenido_en_favoritos = False

        # Pasar el estado de favoritos a la plantilla
        context['contenido_en_favoritos'] = contenido_en_favoritos

        return context




class ActualizarProgresoContenido(LoginRequiredMixin, View):
    def post(self, request, ruta_id, contenido_id):
        # Obtener el contenido y la ruta para el usuario actual
        contenido = get_object_or_404(Contenido, id=contenido_id)
        ruta = get_object_or_404(RutaAprendizaje, id=ruta_id, usuario=request.user)

        # Obtener o crear el progreso del contenido para el usuario en la ruta específica
        progreso, created = ProgresoContenido.objects.get_or_create(
            usuario=request.user,
            contenido=contenido,
            ruta=ruta
        )

        # Verificar si se trata de marcar o desmarcar como completado
        if 'marcar' in request.POST:
            progreso.completado = True
            progreso.fecha_completado = timezone.now()
            calificacion = request.POST.get('calificacion')
            if calificacion:
                progreso.calificacion = int(calificacion)
        elif 'desmarcar' in request.POST:
            progreso.completado = False
            progreso.fecha_completado = None
            progreso.calificacion = None  # Opcional: eliminar calificación si se desmarca

        progreso.save()
        return redirect('ruta_detail', pk=ruta.id)

    
class RutaFavoritasView(ListView):
    model = RutaAprendizaje
    template_name = 'ruta_favoritas.html'
    context_object_name = 'rutas_favoritas'

    def get_queryset(self):
        # Obtener el objeto Favorito del usuario
        favorito = Favorito.objects.filter(usuario=self.request.user).first()
        if favorito:
            # Obtener todas las rutas en la lista de favoritos del usuario
            return favorito.lista.all()
        return RutaAprendizaje.objects.none()  # Devolver un queryset vacío si no tiene favoritos

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, 4)
        page_number = request.GET.get('page')
        rutas_favoritas = paginator.get_page(page_number)
        return render(request, self.template_name, {'rutas_favoritas': rutas_favoritas, 'page_obj': rutas_favoritas})

class RutaEliminarView(ListView):
    model = RutaAprendizaje
    template_name = 'ruta_eliminar.html'
    context_object_name = 'rutas'
    paginate_by = 4

    def get_queryset(self):
        # Show the user's routes for deletion
        return RutaAprendizaje.objects.filter(usuario=self.request.user)

class RutaConfirmarEliminarView(View):
    def post(self, request, *args, **kwargs):
        route_id = request.POST.get('route_id')
        ruta = get_object_or_404(RutaAprendizaje, id=route_id, usuario=request.user)
        ruta.delete()
        messages.success(request, 'Ruta eliminada exitosamente.')
        return redirect('my_routes')  # Redirect to the my routes view


class AgregarAFavoritosView(View):
    def post(self, request, ruta_id):
        usuario = request.user
        contenido = RutaAprendizaje.objects.get(id=ruta_id)
        
        # Verificar si el usuario tiene un favorito
        favorito = Favorito.objects.filter(usuario=usuario).first()
        if favorito:
            if contenido in favorito.lista.all():  # Usamos 'lista' en lugar de 'rutas'
                favorito.lista.remove(contenido)
            else:
                favorito.lista.add(contenido)
        else:
            # Si el usuario no tiene un objeto Favorito, crearlo
            nuevo_favorito = Favorito(usuario=usuario)
            nuevo_favorito.save()
            nuevo_favorito.lista.add(contenido)  # Usamos 'lista' en lugar de 'rutas'

        # Redirigir de nuevo a la misma página de detalle de ruta
        return redirect('ruta_detail', pk=ruta_id)

