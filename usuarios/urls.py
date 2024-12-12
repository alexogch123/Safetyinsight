from django.urls import path
from .views import PuestoList, PuestoNew, PuestoEdit, PuestoDelete

app_name = 'usuarios'

urlpatterns = [
       path('', PuestoList.as_view(), name='puesto_list'),  # Ruta para la lista de puestos
       path('new/', PuestoNew.as_view(), name='puesto_new'),  # Ruta para crear un nuevo puesto
       path('<int:pk>/edit/', PuestoEdit.as_view(), name='puesto_edit'),  # Ruta para editar un puesto   
       path('<int:pk>/delete/', PuestoDelete.as_view(), name='puesto_delete'),  # Ruta para eliminar un puesto
       
]