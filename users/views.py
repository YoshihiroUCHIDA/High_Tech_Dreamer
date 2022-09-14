from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import CustomUser, Follow
from diaries.models import Diary
from . import forms

def index(request):
    users = CustomUser.objects.filter(job="student")
    params = {
        'title': '生徒',
        'users_list': users,
    }
    return render(request, 'users/index.html', params)

def teacher_index(request):
    users = CustomUser.objects.filter(job="teacher")
    params = {
        'title': '講師',
        'users_list': users,
    }
    return render(request, 'users/index.html', params)

def follow_index(request):
    # フォロー中の生徒を取得
    follows_id_list = Follow.objects.filter(owner=request.user).values('follow_target_id').values_list('follow_target_id', flat=True)
    users = CustomUser.objects.filter(id__in=follows_id_list)
    params = {
        'title': '担当生徒',
        'users_list': users,
    }
    return render(request, 'users/index.html', params)

def detail(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    diaries = Diary.objects.filter(student = user)
    birthday = user.birthday
    params = {
        'user': user,
        'diaries_list': diaries,
    }
    return render(request, 'users/detail.html', params)

def follow(request, user_id):
    following = CustomUser.objects.get(pk=user_id)
    Follow.objects.get_or_create(owner=request.user, follow_target=following)
    return HttpResponseRedirect(reverse('users:detail', args=[str(user_id)]))

def edit(request,user_id):
    obj=CustomUser.objects.get(id=user_id)

    if (request.method == 'POST'):
        user = forms.CustomUserCreationForm(request.POST,instance=obj)
        if user.is_valid():
            user.save()
            return redirect(to='/users/index')
        else:
            print("valid failed")

    params = {
        'id': user_id,
        'form': forms.CustomUserCreationForm(instance=obj)
    }
    return render(request,'users/edit.html',params)

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "users/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "users/logout.html"
