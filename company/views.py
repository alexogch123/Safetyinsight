"""
Views for the company app.

This module contains class-based views for handling organization
CRUD operations and list display.
"""
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Organization
from .forms import OrganizationForm


class OrganizationView(LoginRequiredMixin, generic.ListView):
    """
    View for displaying a list of organizations.

    This view requires user authentication and displays all active
    organizations in the system.

    Attributes:
        model: The Organization model to list.
        template_name: The template to render the list.
        context_object_name: Name of the context variable in template.
        login_url: URL to redirect if user is not authenticated.
    """
    model = Organization
    template_name = "company/company_list.html"
    context_object_name = "obj"
    login_url = "bases:login"


class OrganizationNew(LoginRequiredMixin, generic.CreateView):
    """
    View for creating new organizations.

    Handles the creation of new organization records, requiring
    user authentication.

    Attributes:
        model: The Organization model.
        template_name: Template for the creation form.
        form_class: Form class to use for data input.
        success_url: URL to redirect after successful creation.
    """
    model = Organization
    template_name = "company/company_form.html"
    context_object_name = "obj"
    form_class = OrganizationForm
    success_url = reverse_lazy("company:company_list")
    login_url = "bases:login"

    def form_valid(self, form):
        """
        Process the form if valid.

        Adds the current user as the creator of the record.

        Args:
            form: The validated form instance.

        Returns:
            HttpResponse: Redirect to success URL.
        """
        form.instance.uc = self.request.user
        return super().form_valid(form)


class OrganizationEdit(LoginRequiredMixin, generic.UpdateView):
    """
    View for editing existing organizations.

    Handles the modification of organization records, requiring
    user authentication.

    Attributes:
        model: The Organization model.
        template_name: Template for the edit form.
        form_class: Form class to use for data input.
        success_url: URL to redirect after successful update.
    """
    model = Organization
    template_name = "company/company_form.html"
    context_object_name = "obj"
    form_class = OrganizationForm
    success_url = reverse_lazy("company:company_list")
    login_url = "bases:login"

    def form_valid(self, form):
        """
        Process the form if valid.

        Adds the current user as the modifier of the record.

        Args:
            form: The validated form instance.

        Returns:
            HttpResponse: Redirect to success URL.
        """
        form.instance.um = self.request.user
        return super().form_valid(form)


class OrganizationDelete(LoginRequiredMixin, SuccessMessageMixin, generic.View):
    """
    View for deactivating organizations.

    Instead of deleting records, this view marks organizations as inactive
    and tracks who made the change.

    Attributes:
        model: The Organization model.
        success_url: URL to redirect after successful deactivation.
        success_message: Message to display after successful deactivation.
    """
    model = Organization
    success_url = reverse_lazy("company:company_list")
    success_message = "Organización desactivada correctamente"

    def get(self, request, pk=None):
        """
        Handle GET request to deactivate an organization.

        Args:
            request: The HTTP request.
            pk: Primary key of the organization to deactivate.

        Returns:
            HttpResponse: Redirect to the organization list.
        """
        organization = Organization.objects.filter(pk=pk).first()
        if organization:
            organization.estado = False
            organization.um = request.user
            organization.save()
            messages.success(request, self.success_message)
        else:
            messages.error(request, "Organización no encontrada")
        return redirect("company:company_list")


class CompanyList(generic.ListView):
    model = Organization
    template_name = "company/company_list.html"
    context_object_name = "obj"


class CompanyNew(generic.CreateView):
    model = Organization
    template_name = "company/company_form.html"
    context_object_name = "obj"
    success_url = reverse_lazy("company:company_list")
    fields = ['name', 'status']


class CompanyEdit(generic.UpdateView):
    model = Organization
    template_name = "company/company_form.html"
    context_object_name = "obj"
    success_url = reverse_lazy("company:company_list")
    fields = ['name', 'status']


class CompanyDel(generic.DeleteView):
    model = Organization
    template_name = 'company/company_del.html'
    context_object_name = "obj"
    success_url = reverse_lazy("company:company_list")

