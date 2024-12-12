from django.db import models
from django.contrib.auth.models import User

class Puesto(models.Model):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del puesto'
    )
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    um = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True, blank=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'
        ordering = ['descripcion']