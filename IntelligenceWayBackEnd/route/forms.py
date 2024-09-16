from django import forms
from .models import rutaAprendizaje
from .models import LearningPreferences

"""
class UsuarioForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Usuario
        fields = ["nombre", "correo", "password"]
        
        def clean(self):
            cleaned_data = super(UsuarioForm, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                raise forms.ValidationError("password and confirm_password does not match")
   
"""          

class AprendizajeForm(forms.ModelForm):
    class Meta:
        model = rutaAprendizaje
        fields = ['title','description']



class LearningPreferencesForm(forms.ModelForm):
    class Meta:
        model = LearningPreferences
        fields = ['preferred_language', 'learning_style']

        