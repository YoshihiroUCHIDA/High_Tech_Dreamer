from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms

from .models import CustomUser
from diaries.models import Diary

# Create your views here.

def index(request):
    users = CustomUser.objects.filter(job="student")
    params = { 'users_list': users,}
    return render(request, 'users/index.html', params)

def detail(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    diaries = Diary.objects.filter(student_id=user.id)
    params = { 
            'user': user,
            'diaries_list' : diaries,
        }
    return render(request, 'users/detail.html', params)

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "users/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "users/logout.html"

#class IndexView(TemplateView):
#    template_name = "users/detail.html"
