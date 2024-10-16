from django import forms

class interesForm(forms.Form):
        class Meta:
            interes=forms.CharField(max_length=50)
            


