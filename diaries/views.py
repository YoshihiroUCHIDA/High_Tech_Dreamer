from django.shortcuts import render
from django.shortcuts import redirect
from diaries.models import Diary
from .forms import DiaryForm

# --------------------------------------------------
# 日報リストの表示
def index(request):
    diary = Diary.objects.all()
    params = {
        'diaries_list': diary,
    }
    return render(request, 'diaries/index.html', params)

# --------------------------------------------------
# 特定の日報の表示
def detail(request, diary_id):
    diary = Diary.objects.get(pk=diary_id)
    params = {
        'diary': diary,
    }
    return render(request, 'diaries/detail.html', params)

# --------------------------------------------------
# 日報の作成
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

# --------------------------------------------------
# 日報の編集
def edit(request, diary_id):
    obj = Diary.objects.get(id=diary_id)
    
    if (request.method == 'POST'):
        diary = DiaryForm(request.POST, instance=obj)
        diary.save()
        return redirect(to='/diaries')

    params = {
        'id': diary_id,
        'form': DiaryForm(instance=obj)
    }
    return render(request, 'diaries/edit.html', params)

# --------------------------------------------------
# 日報の削除
def delete(request, diary_id):
    diary = Diary.objects.get(id=diary_id)
    
    if (request.method == 'POST'):
        diary.delete()
        return redirect(to='/diaries')
    
    params = {
        'id': diary_id,
        'diary': diary,
    }
    return render(request, 'diaries/delete.html', params)
