from django import forms
from .models import Tag, Reporte
'''
class InteresForm(forms.Form):
    interes =forms.CharField(max_length=50)
'''
            


class InteresForm(forms.Form):
    interes = forms.ChoiceField(choices=[], label="Selecciona una categoría")

    def __init__(self, *args, **kwargs):
        super(InteresForm, self).__init__(*args, **kwargs)
        # Obtener las opciones desde el modelo Categoria
        self.fields['interes'].choices = [(interes.id, interes.tagName) for interes in Tag.objects.all()]
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            
class ReporteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReporteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Reporte
        fields = ['descripcion']  # Solo permitirá agregar la descripción
        labels = {
            'descripcion': 'Descripción del problema',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }