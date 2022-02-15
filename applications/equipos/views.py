from django.shortcuts import render
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import EquiposModel

class EquiposListView(LoginRequiredMixin,ListView):
    template_name = "equipos/lista-equipos.html"
    model = EquiposModel
    context_object_name = 'equipos'
    paginate_by = 8
    login_url = "home_app:login"

class EquiposDetailView(LoginRequiredMixin,DetailView):
    template_name = "equipos/detalle-equipo.html"
    model = EquiposModel
    context_object_name = "detalle"