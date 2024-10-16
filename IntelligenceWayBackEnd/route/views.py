from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InteresForm
from .models import Contenido, RutaAprendizaje, Tag
from .algoritmo import VerificacionContenido,VerificacionTiempo
from user.models import User

class CreateRoute(View):
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
