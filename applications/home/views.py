from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout
from django.views.generic.edit import (
    FormView,
)
from django.views.generic import (
    View,
    TemplateView
)
from .forms import LoginForm

class LoginView(FormView):
    form_class = LoginForm
    template_name = "home/login.html"
    # next_page = reverse_lazy('.')
    success_url = reverse_lazy('equipos_app:equipos')

    def form_valid(self,form):

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        usuario = authenticate(
            username=username,
            password=password
        )

        login(self.request,usuario)

        next = self.request.POST.get('next','/')

        print('********',next)

        if(next != '/'):
            return HttpResponseRedirect(next)

        return super(LoginView,self).form_valid(form)

class LogOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)

        return HttpResponseRedirect(
            reverse(
                'home_app:login'
            )
        )
    
class HomeView(TemplateView):
    template_name = "home/home-page.html"

    
    
