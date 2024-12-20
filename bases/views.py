from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView

class Home(LoginRequiredMixin,TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'
