from django.shortcuts import render
from django.http import HttpResponse

import jukus
from .models import Juku

def top(request):
    jukus = Juku.objects.all
    context = { 'jukus_news': jukus,}
    return render(request, 'jukus/top.html', context)

def detail(request, juku_id):
    juku = Juku.objects.get(pk=juku_id)
    context = { 'juku': juku,}
    return render(request, 'jukus/detail.html', context)

# Create your views here.
