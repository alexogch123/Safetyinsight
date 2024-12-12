from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Puesto
from .forms import PuestoForm
from django.contrib import messages
from django.shortcuts import render, redirect

class PuestoList(LoginRequiredMixin, generic.ListView):
    model = Puesto
    template_name = "usuarios/puesto_list.html"
    context_object_name = "puestos"

class PuestoNew(LoginRequiredMixin, generic.CreateView):
    model = Puesto
    template_name = "usuarios/puesto_form.html"
    form_class = PuestoForm
    success_url = reverse_lazy("usuarios:puesto_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class PuestoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Puesto
    template_name = "usuarios/puesto_form.html"
    form_class = PuestoForm
    success_url = reverse_lazy("usuarios:puesto_list")

    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)




class PuestoDelete(LoginRequiredMixin, SuccessMessageMixin, generic.View):

    model = Puesto
    success_url = reverse_lazy("usuarios:puesto_list")
    success_message = "Puesto desactivada correctamente"

    def get(self, request, pk=None):
 
        puesto = Puesto.objects.filter(pk=pk).first()
        if puesto:
            puesto.estado = False
            puesto.um = request.user
            puesto.save()
            messages.success(request, self.success_message)
        else:
            messages.error(request, "Puesto no encontrado")
        return redirect("usuarios:puesto_list")

