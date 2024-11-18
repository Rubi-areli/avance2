from django import forms
from .models import Adoptante

class AdoptanteForm(forms.ModelForm):
    class Meta:
        model = Adoptante
        fields = ['nombre', 'telefono', 'correo', 'direccion']
