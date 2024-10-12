from django import forms
from .models import rutaAprendizaje, formularioAprendizajeUsuario, CustomUser


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
    created_at = forms.DateField(required=False)
    update_at = forms.DateField(required=False)
    
    class Meta:
        model = formularioAprendizajeUsuario
        fields = [ "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]


class LearningPreferencesForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["preferred_language", "learning_style"]   
        