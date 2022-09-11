from django.shortcuts import render
from django.http import HttpResponse

import jukus
from .models import Juku
from users.models import CustomUser
from diaries.models import Diary

def dashboard(request, juku_id):
    juku = Juku.objects.get(pk=juku_id)
    context = { 
        'juku': juku,
        'users_list' : CustomUser.objects.all(),
        'diaries_list' : Diary.objects.all(),
    }
    return render(request, 'jukus/dashboard.html', context)

# Create your views here.
