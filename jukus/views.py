import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Juku
from users.models import CustomUser
from users.models import Follow
from diaries.models import Diary

from contributions_django.graphs import generate_contributors_graph
from contributions_django import dateutils

@login_required
def dashboard(request):
    user = request.user
    juku = Juku.objects.get(pk=user.juku_id)

    following = Follow.objects.filter(owner=user)
    following_list = []
    i = 0
    while i < 4 and i < len(following):
        following_list.append(following[i].follow_target)
        i += 1

    dates = Diary.objects.values_list('date', flat=True)
    graph_data = generate_contributors_graph(dates)

    if user.job == "student":
        diaries_list = Diary.objects.filter(student_id=user.id).order_by("date").reverse()[0:4]
    else:
        diaries_list = Diary.objects.all().order_by("date").reverse()[0:4]

    params = { 
        'juku': juku,
        'user' : user,
        'users_list' : following_list,
        'diaries_list' : diaries_list,
        'contributions_django' : graph_data,
        'month_ago_date' : (datetime.date.today() - datetime.timedelta(30)).strftime("%Y-%m-%d")
    }

    return render(request, 'jukus/dashboard.html', params)
