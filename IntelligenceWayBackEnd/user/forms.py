from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password2'].label = ""
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = User
        fields = ['nombre', 'email', 'password1', 'password2']
        
        
class LoginForm(AuthenticationForm):
    def __init__(self, request = ..., *args, **kwargs):
        super(LoginForm, self).__init__(request, *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        