from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser
from diaries.models import Diary

# Create your views here.

def index(request):
    users = CustomUser.objects.all()
    params = { 'users_list': users,}
    return render(request, 'users/index.html', params)

def detail(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    diaries = Diary.objects.filter(student_id=user_id)
    params = { 
            'user': user,
            'diaries_list' : diaries,
        }
    return render(request, 'users/detail.html', params)
