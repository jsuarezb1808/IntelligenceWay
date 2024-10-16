from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import AprendizajeForm
from django.views import View
from django.views.generic.edit import UpdateView
from .models import ModeloAprendizajeUsuario
from route.algoritmo import EstimacionEstudio




# Create your views here.
class FormularioView(LoginRequiredMixin, UpdateView):
    model = ModeloAprendizajeUsuario
    form_class = AprendizajeForm
    template_name = 'test.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        return ModeloAprendizajeUsuario.objects.get(usuario=self.request.user)
    

class RespuestasView(View):
    def post(self, request):
        form = AprendizajeForm()
        return render(request, 'respuestas_form.html', {'form': form})

    def get(self, request):
            Estimacion=EstimacionEstudio



            modelo=ModeloAprendizajeUsuario.objects.get(usuario=request.user)
            # Obtener las respuestas del modelo de aprendizaje
            user_responses=modelo
            # Llamar algoritmo para obtener preferencias
            preferencias_contenido = Estimacion.PreferenciasContenido(user_responses)
            preferencias_tiempo = Estimacion.PreferenciasTiempo(user_responses)

            # Actualizar los campos del usuario
            
            user = request.user
            user.PreferenciasAudio = preferencias_contenido[1]
            user.PreferenciasVideo = preferencias_contenido[2]
            user.PreferenciasTexto = preferencias_contenido[0]
            user.PreferenciasTiempo = preferencias_tiempo  # Asegúrate de que este campo existe
            user.save()

            return redirect('profile')

       