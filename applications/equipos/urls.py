from django.urls import path
from .views import *

app_name = "equipos_app"

urlpatterns = [
    path('lista-equipos/',EquiposListView.as_view(),name="equipos"),
    path('detalles/<pk>/',EquiposDetailView.as_view(),name="detalles"),
]
