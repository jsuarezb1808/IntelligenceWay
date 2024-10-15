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
    def get(self, request):
        form = AprendizajeForm()
        return render(request, 'respuestas_form.html', {'form': form})

    def post(self, request):
        form = AprendizajeForm(request.POST)
        if form.is_valid():
            user_responses = ModeloAprendizajeUsuario.objects.get(usuario=self.request.user)
            user_responses.q1 = form.cleaned_data['q1']
            user_responses.q2 = form.cleaned_data['q2']
            user_responses.q3 = form.cleaned_data['q3']
            user_responses.q4 = form.cleaned_data['q4']
            user_responses.q5 = form.cleaned_data['q5']
            user_responses.q6 = form.cleaned_data['q6']
            user_responses.q7 = form.cleaned_data['q7']
            user_responses.q8 = form.cleaned_data['q8']


            # Llamar algoritmo
            preferencias_contenido = EstimacionEstudio.PreferenciasContenido(user_responses.q1, user_responses.q2, user_responses.q3, user_responses.q5, user_responses.q6, user_responses.q7)
            preferencias_tiempo = EstimacionEstudio.PreferenciasTiempo(user_responses.q4, user_responses.q8)

            # Guarda los resultados en la tabla user
            user = request.user
            user.content = preferencias_contenido
            user.tiempo = preferencias_tiempo
            user.save()

            return redirect('profile')
        return render(request, 'respuestas_form.html', {'form': form})