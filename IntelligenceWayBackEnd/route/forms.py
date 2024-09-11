from django import forms
from .models import rutaAprendizaje, formularioAprendizajeUsuario

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
        fields = ["usuario", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]
        