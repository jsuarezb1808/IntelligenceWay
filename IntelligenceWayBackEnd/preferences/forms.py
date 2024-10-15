from django import forms
from .models import ModeloAprendizajeUsuario

class AprendizajeForm(forms.ModelForm):
    CHOICES = [
        (1, 'Nunca'),
        (2, 'Poco frecuente'),
        (3, 'Normalmente no'),
        (4, 'Frecuentemente'),
        (5, 'Siempre'),
    ]
    CHOICES2 = [
        (1, 'Menos de 1 hora'),
        (2, '1 hora'),
        (3, 'Entre 1 y 2 horas'),
        (4, 'Entre 2 y 3 horas'),
        (5, 'Más de 3 horas')
    ]
    q1 = forms.ChoiceField(choices=CHOICES,)
    q2 = forms.ChoiceField(choices=CHOICES,)
    q3 = forms.ChoiceField(choices=CHOICES,)
    q4 = forms.ChoiceField(choices=CHOICES2,)
    q5 = forms.ChoiceField(choices=CHOICES,)
    q6 = forms.ChoiceField(choices=CHOICES,)
    q7 = forms.ChoiceField(choices=CHOICES,)
    q8 = forms.ChoiceField(choices=CHOICES2,)
    
    
    def __init__(self, *args, **kwargs):
        super(AprendizajeForm, self).__init__(*args, **kwargs)
        self.fields['q1'].label = "¿Qué tan frecuentemente usas libros, papers y artículos para estudiar?"
        self.fields['q2'].label = "¿Qué tan frecuentemente usas audiolibros, podcasts o contenido de audio en general para estudiar?"
        self.fields['q3'].label = "¿Qué tan frecuentemente usas videos, documentales o listas de reproducción para estudiar?"
        self.fields['q4'].label = "¿Qué tanto tiempo dedicas a estudiar?"
        self.fields['q5'].label = "¿Qué tan frecuentemente consumes contenido como historias, libros o novelas en tu tiempo libre?"
        self.fields['q6'].label = "¿Qué tan frecuentemente escuchas podcasts, programas de entrevistas o audiolibros en tu tiempo libre?"
        self.fields['q7'].label = "¿Qué tan frecuentemente ves contenido en páginas como YouTube, Instagram, TikTok, etc.?"
        self.fields['q8'].label = "¿Qué tanto tiempo dedicas a tus pasatiempos?"
        
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            
    class Meta:
        model = ModeloAprendizajeUsuario
        fields = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]
        