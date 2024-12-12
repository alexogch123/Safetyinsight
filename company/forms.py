"""
Forms for the company app.

This module contains form classes for handling organization data input
and validation.
"""
from django import forms
from .models import Organization, Direction, Plant


class OrganizationForm(forms.ModelForm):
    """
    Form for creating and updating Organization instances.

    This form handles the input and validation of organization data,
    including automatic conversion of description to uppercase.

    Attributes:
        model: The Organization model this form is based on.
        fields: List of fields to include in the form.
        labels: Custom labels for form fields.
        widgets: Custom widgets for form fields.
    """

    class Meta:
        """
        Meta class for OrganizationForm configuration.
        """
        model = Organization
        fields = '__all__'  # O especifica los campos que necesitas

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and add Bootstrap classes to all fields.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_descripcion(self):
        """
        Clean and transform the description field value.

        Converts the description text to uppercase before saving.

        Returns:
            str: The uppercase version of the description text.
        """
        return self.cleaned_data['descripcion'].upper()


class DirectionForm(forms.ModelForm):
    """Form for creating and updating Direction instances."""
    
    class Meta:
        model = Direction
        fields = '__all__'

    def clean(self):
        """Clean all text fields to uppercase and validate required fields."""
        cleaned_data = super().clean()
        
        # Validación para asegurarse de que los campos no estén vacíos
        for field in ['calle', 'numero_exterior', 'numero_interior', 'colonia', 'codigo_postal', 'ciudad', 'estado', 'pais']:
            if not cleaned_data.get(field):
                self.add_error(field, 'Este campo es obligatorio.')
        
        # Lista de campos a convertir a mayúsculas
        text_fields = [
            'calle', 'numero_exterior', 'numero_interior',
            'colonia', 'codigo_postal', 'ciudad', 'estado', 'pais'
        ]
        
        for field in text_fields:
            if cleaned_data.get(field):
                cleaned_data[field] = cleaned_data[field].upper()
        
        return cleaned_data

    def __init__(self, *args, **kwargs):
        """Initialize the form."""
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class PlantForm(forms.ModelForm):
    """Form for creating and updating Plant instances."""
    
    class Meta:
        model = Plant
        fields = '__all__'

    def clean(self):
        """Clean all text fields to uppercase and validate required fields."""
        cleaned_data = super().clean()
        
        # Validación para asegurarse de que los campos no estén vacíos
        for field in ['name', 'description']:
            if not cleaned_data.get(field):
                self.add_error(field, 'Este campo es obligatorio.')
        
        # Lista de campos a convertir a mayúsculas
        text_fields = ['name', 'description']
        
        for field in text_fields:
            if cleaned_data.get(field):
                cleaned_data[field] = cleaned_data[field].upper()
        
        return cleaned_data

    def __init__(self, *args, **kwargs):
        """Initialize the form."""
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    