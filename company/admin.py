from django.contrib import admin
from .models import Organization, Direction

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    """Admin configuration for Direction model."""
    list_display = ['calle', 'numero_exterior', 'colonia', 'ciudad', 'organization', 'estado']
    list_filter = ['organization', 'ciudad', 'estado']
    search_fields = ['calle', 'colonia', 'ciudad']
