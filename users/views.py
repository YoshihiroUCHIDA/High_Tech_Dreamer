import datetime

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import CustomUser, Follow
from diaries.models import Diary
from . import forms

# Create your views here.


def index(request):
    users = CustomUser.objects.filter(job="student")
    params = {'users_list': users,}
    return render(request, 'users/index.html', params)

<<<<<<< HEAD
=======
def teacher_index(request):
    users = CustomUser.objects.filter(job="teacher")
    params = { 'users_list': users,}
    return render(request, 'users/teacher_index.html', params)

>>>>>>> b7a9b9c0e441704d27e315c912bebd4936ddde3b
def detail(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    diaries = Diary.objects.filter(student = user)
    birthday = user.birthday
    grade = ConvertToGrade(birthday)

    params = {
        'user': user,
        'user_grade':grade,
        'diaries_list': diaries,
    }

    return render(request, 'users/detail.html', params)

<<<<<<< HEAD
def ConvertToGrade(today, birthday):
    a = "0401"
    birthmd = birthday.strftime("%Y%m%d")[4:]
    birthy= birthday.strftime("%Y%m%d")[0:4]
    todayy=today.strftime("%Y%m%d")[0:4]
    if int(birthmd) < int(a) :#早生まれ
        g=int(todayy)-int(birthy)
    else:#遅生まれ
        g=int(todayy)-int(birthy)-1
    grade=""
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

=======
def follow(request, user_id):
    following = CustomUser.objects.get(pk=user_id)
    Follow.objects.get_or_create(owner=request.user, follow_target=following)

    return HttpResponseRedirect(reverse('users:detail', args=[str(user_id)]))

def ConvertToGrade(birthday):
    print(birthday)
    birth_y = birthday.year
    birth_m = birthday.month
    today_y = datetime.date.today().year

    if birth_m < 4:
        g = today_y - birth_y
    else:           #遅生まれ
        g = today_y - birth_y - 1

    grade = "999"
    if g == 6:
        grade = "小学1年生"
    elif g == 7:
        grade = "小学2年生"
    elif g == 8:
        grade = "小学3年生"
    elif g == 9:
        grade = "小学4年生"
    elif g == 10:
        grade = "小学5年生"
    elif g == 11:
        grade = "小学6年生"
    elif g == 12:
        grade = "中学1年生"
    elif g == 13:
        grade = "中学2年生"
    elif g == 14:
        grade = "中学3年生"
    elif g == 15:
        grade = "高校1年生"
    elif g == 16:
        grade = "高校2年生"
    elif g == 17:
        grade = "高校3年生"

    return grade

def edit(request,user_id):
    obj=CustomUser.objects.get(id=user_id)

    if(request.method=='POST'):
        user=forms.CustomUserCreationForm(request.POST,instance=obj)
        user.save()
        return redirect(to='/users')
    params={
        'id':user_id,
        'form':forms.CustomUserCreationForm(instance=obj)
    }
    return render(request,'users/edit.html',params)

>>>>>>> b7a9b9c0e441704d27e315c912bebd4936ddde3b

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "users/login.html"


class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "users/logout.html"
