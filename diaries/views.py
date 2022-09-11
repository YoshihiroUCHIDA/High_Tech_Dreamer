from django.shortcuts import render
from django.shortcuts import redirect
from diaries.models import Diary
from .forms import DiaryForm

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

# --------------------------------------------------
def create(request):
    if (request.method == 'POST'):
        obj = Diary()
        diary = DiaryForm(request.POST, instance=obj)
        diary.save()
        return redirect(to='/diaries')

    params = {
        'form': DiaryForm(),
    }
    return render(request, 'diaries/create.html', params)