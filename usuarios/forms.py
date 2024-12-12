from django import forms
from .models import Puesto

class PuestoForm(forms.ModelForm):
    """Formulario para crear y editar puestos."""
    class Meta:
        model = Puesto
        fields = ['descripcion', 'estado']
        labels = {
            'descripcion': 'Descripción del Puesto',
            'estado': 'Estado'
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del puesto'
            }),
            'estado': forms.CheckboxInput(attrs={
                'class': 'form-control'
            })
        } 