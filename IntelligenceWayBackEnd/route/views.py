from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InteresForm
from .models import Contenido, RutaAprendizaje, Tag, Favorito
from .algoritmo import VerificacionContenido, VerificacionTiempo
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
        # Redirect to the same page after submitting the report
        return reverse('contenido_detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            # Create the report
            reporte = form.save(commit=False)
            reporte.IdContenido = self.object
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
            # Get the interest from the form
            interes = form.cleaned_data['interes']

            # Get the courses that match the interest
            cursos = Contenido.objects.filter(tags=interes)

            # Initialize the list of valid contents
            contenidos_validos = []

            user = request.user
            
            # Filter courses that meet the conditions
            for curso in cursos:
                if VerificacionContenido(curso, User.objects.get(id=user.id)) and \
                   VerificacionTiempo(curso, User.objects.get(id=user.id)):
                    contenidos_validos.append(curso)
            nombreTag = Tag.objects.get(id=interes).tagName
            # Create the new learning route
            ruta = RutaAprendizaje(
                title=nombreTag,
                description=f"Una ruta enfocada en conocimientos relacionados a {nombreTag}",
                usuario=request.user
            )
            ruta.save()

            # Assign the contents to the route using set()
            ruta.contenidos.set(contenidos_validos)
            ruta.save()

            return redirect("my_routes")
        else:
            return render(request, self.template_name, viewData)

class MyRoutes(ListView):
    model = RutaAprendizaje
    template_name = 'my_routes.html'  # Change this to the path to your template
    context_object_name = 'routes'
    paginate_by = 4  # Number of routes per page

    def get_queryset(self):
        # Filter the routes of the current user
        return RutaAprendizaje.objects.filter(usuario=self.request.user)  # Make sure to filter by user

class RutaDetail(LoginRequiredMixin, DetailView):
    model = RutaAprendizaje
    template_name = 'ruta_detail.html'  # Make sure this is the path to your detail template
    context_object_name = 'route'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the contents of the route to the context
        context['contenidos'] = self.object.contenidos.all()
        return context

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
