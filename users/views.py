from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms

from .models import CustomUser
from diaries.models import Diary
import datetime

# Create your views here.


def index(request):
    users = CustomUser.objects.filter(job="student")
    params = {'users_list': users, }
    return render(request, 'users/index.html', params)


def detail(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    diaries = Diary.objects.filter(student = user)
    today = datetime.date.today()
    birthday = user.birthday
    grade=ConvertToGrade(today, birthday)

    params = {
        'user': user,
        'diaries_list': diaries,
        'user_grade':grade,
    }

    return render(request, 'users/detail.html', params)


def ConvertToGrade(today, birthday):
    a = "0401"
    birthmd = birthday.strftime("%Y%m%d")[4:]
    birthy= birthday.strftime("%Y%m%d")[0:4]
    todayy=today.strftime("%Y%m%d")[0:4]
    if int(birthmd) < int(a) :#早生まれ
        g=int(todayy)-int(birthy)
    else:#遅生まれ
        g=int(todayy)-int(birthy)-1
    grade="不明"
    if g==6:
        grade="小学1年生"
    elif g==7:
        grade="小学2年生"
    elif g==8:
        grade="小学3年生"
    elif g==9:
        grade="小学4年生"
    elif g==10:
        grade="小学5年生"
    elif g==11:
        grade="小学6年生"
    elif g==12:
        grade="中学1年生"
    elif g==13:
        grade="中学2年生"
    elif g==14:
        grade="中学3年生"
    elif g==15:
        grade="高校1年生"
    elif g==16:
        grade="高校2年生"
    elif g==17:
        grade="高校3年生"

    return grade


class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "users/login.html"


class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "users/logout.html"

# class IndexView(TemplateView):
#    template_name = "users/detail.html"
