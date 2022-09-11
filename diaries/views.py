from django.shortcuts import render
from .models import Diary

# --------------------------------------------------
def index(request):
    diary = Diary.objects.all()
    params = {
        'diary_list': diary,
    }
    return render(request, 'diaries/index.html', params)

# --------------------------------------------------
def detail(request, diary_id):
    diary = Diary.objects.get(pk=diary_id)
    params = {
        'diary': diary,
    }
    return render(request, 'diaries/detail.html', params)
