from django.shortcuts import render
from django.http import HttpResponse

from .models import Juku
from users.models import CustomUser
from users.models import Follow
from diaries.models import Diary

def dashboard(request):
    user = request.user
    following = Follow.objects.filter(owner=user)
    following_list = []
    for f in following:
        following_list.append(f.follow_target)
    juku = Juku.objects.get(pk=user.juku_id)
    if user.job == "student":
        #自分が生徒の場合は自分について書かれた日報のみ
        diaries_list = Diary.objects.filter(student_id=user.id).order_by("date").reverse()[0:4]
    else:
        diaries_list = Diary.objects.all().order_by("date").reverse()[0:4]

    params = { 
        'juku': juku,
        'user' : user,
        'users_list' : following_list,
        'diaries_list' : diaries_list
    }
    return render(request, 'jukus/dashboard.html', params)
