from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms

# Create your views here.

def index(request):
    users = CustomUser.objects.all()
    context = { 'users_list': users,}
    return render(request, 'users/index.html', context)

def detail(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    context = { 'user': user,}
    return render(request, 'users/detail.html', context)

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "users/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "users/logout.html"

class IndexView(TemplateView):
    template_name = "users/index.html"
