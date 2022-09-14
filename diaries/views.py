import datetime
from contributions_django.graphs import generate_contributors_graph

from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from .forms import DiaryForm
from .models import Diary
from users.models import CustomUser


# --------------------------------------------------
# 日報リストの表示
def index(request):
    diary = Diary.objects.all().order_by("date").reverse()
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
    # Submit の処理
    if (request.method == 'POST'):
        diary = DiaryForm(request.POST)
        diary.save()
        return redirect(to='/diaries')

    # 現在の講師ユーザの情報を取得
    teacher = CustomUser.objects.get(id=request.user.id)
    diary_form = DiaryForm(initial={'teacher': teacher})

    # 初期値の設定
    params = {
        'form': diary_form,
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
#芝生の表示
def heatmap(request):
    dates = Diary.objects.values_list('date', flat=True)
    context = generate_contributors_graph(dates, title="Contributions")
    return render(request, "diaries/heatmap.html", context)

"""
def get(request):
    print("diaryyyyy")

    today = datetime.date.today()
    d = today - datetime.timedelta(days=365)
    data  = []
    for in range(365):
        d += datetime.timedelta(days=1) 
        data.appen({'date': d, 'count': count})

    if request.headers.get("Content-Type") == "application/json":
        diaries = list(Diary.objects.filter(teacher=request.user).values())
        print("diary")
        print(diaries)
        return JsonResponse(diaries, safe=False, status=200)
"""

# --------------------------------------------------
# 日報の削除
@require_POST
def delete(request, diary_id):
    diary = Diary.objects.get(id=diary_id)
    diary.delete()
    return redirect(to='/diaries')
