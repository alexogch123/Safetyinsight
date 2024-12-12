"""
Models for the company app.

This module contains the models related to company organization management.
It includes the Organization model which inherits from ClaseModelo.
"""
from typing import Iterable
from django.db import models
from django.contrib.auth.models import User

from bases.models import ClaseModelo

class Organization(ClaseModelo):
    """
    Model to store organization information.

    This model represents organizations in the system, storing their basic
    information such as name and description.

    Attributes:
        nombre (str): The name of the organization. Must be unique.
        descripcion (str): A detailed description of the organization.
        estado (bool): Indicates if the organization is active.
    """

    nombre = models.CharField(
        max_length=100,
        help_text='Nombre de la Organización',
        unique=True
    )
    descripcion = models.CharField(
        max_length=300,
        help_text='Descripción de la organización',
        null=True,
        blank=True
    )
    uc = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_organizations')
    um = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_organizations')

    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre=self.nombre.upper()
        super(Organization, self).save()

    class Meta:
        """
        Meta class for Organization model.

        Provides additional model configuration including
        verbose names and ordering.
        """
        verbose_name = 'Organización'
        verbose_name_plural = 'Organizaciones'
        ordering = ['nombre']

class Direction(ClaseModelo):
    """Model to store address information."""
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=10)
    numero_interior = models.CharField(max_length=10, blank=True, null=True)
    colonia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        """String representation of the Direction."""
        return f"{self.calle} {self.numero_exterior}, {self.colonia}, {self.ciudad}"

    class Meta:
        """Meta class for Direction model."""
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'
        ordering = ['organization', 'ciudad']

class Plant(ClaseModelo):
    """
    Model to store plant information.

    This model represents plants in the system, storing their
    basic information and status.

    Attributes:
        name (str): Plant name
        description (str): Plant description
        organization (Organization): Related organization
        address (Direction): Plant address
    """
    name = models.CharField(
        max_length=100,
        help_text='Nombre de la planta',
        unique=True
    )
    description = models.CharField(
        max_length=200,
        help_text='Descripción de la planta'
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        help_text='Organización a la que pertenece'
    )
    address = models.ForeignKey(
        Direction,
        on_delete=models.CASCADE,
        help_text='Dirección de la planta'
    )

    def __str__(self):
        """String representation of the Plant."""
        return f'{self.name} - {self.organization}'

    def save(self, *args, **kwargs):
        """Save method for Plant model."""
        self.name = self.name.upper()
        self.description = self.description.upper()
        super(Plant, self).save(*args, **kwargs)

    class Meta:
        """Meta class for Plant model."""
        verbose_name = 'Planta'
        verbose_name_plural = 'Plantas'
        ordering = ['name']