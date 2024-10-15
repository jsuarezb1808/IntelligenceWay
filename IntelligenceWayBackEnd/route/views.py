from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import interesForm
from .models import Contenido,RutaAprendizaje
from .algoritmo import EstimacionEstudio
from user.models import User

#se encarga de crear la ruta una vez el usuario ingresa un interes
class CreateRoute(View):
    template_name = "form.html"
    def get(self,request):
        if not request.user.is_authenticated:
            form = interesForm() 
            viewData = {}
            viewData["form"] = form
            return render(request, self.template_name, viewData)
        return redirect('')

    def post(self, request):
        form = interesForm(data=request.POST) 
        viewData = {}
        viewData["form"] = form
        #confirmamos que la form es valida
        if form.is_valid(): 
            NuevaRuta=None
            #una vez confirmada que la informacion es valida se accede a la info del form
            interes=form.cleaned_data['interes']

            #accedemos a la base de datos y filtramos por los cursos que tengan el interes
            cursos=Contenido.objects.filter(tags=interes)

            #recorremos los elementos que tienen un match para evaluar si cumplen 
            #con el tipo de contenido 
            for curso in cursos:

                #revisamos que cumpla con las condiciones de tipo de contenido y 
                #en caso de no cumplir pasa al siguiente elemento
                user=request.user.id
                if EstimacionEstudio.VerificacionContenido(
                curso,
                User.objects.filter(id=user)
                ):
                    
                    #revisamos que cumpla con las condiciones de tipo de contenido y 
                    #en caso de no cumplir pasa al siguiente elemento
                    if EstimacionEstudio.VerificacionTiempo(
                    curso,
                    User.objects.filter(id=user)
                    ):
                       
                       NuevaRuta=NuevaRuta+','+curso.id
                    #si no cumple la condicion de el tiempo se ignora y continua el programa
                    else:
                        pass
                #si la condicion no se cumple se ignora y continua el programa
                else:
                    pass

            #se crea la ruta de aprendizaje segun la nueva ruta
            ruta=RutaAprendizaje(
                title=interes,
                description=("una rama de contenido enfocado en"+interes),
                usuario=request.user.id,
                contenidos=NuevaRuta,
                completado=False
                )
            ruta.save()
                
            return redirect()
        else:
            form = interesForm() 
            return render(request, self.template_name, viewData)