from django.urls import path,include
from .views import *

app_name = 'home_app'

urlpatterns = [
    path('',LoginView.as_view(),name="home"),
    path('accounts/login/',LoginView.as_view(),name="login"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogOutView.as_view(),name="logout"),
]
