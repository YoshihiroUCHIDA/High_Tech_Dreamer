from django.shortcuts import render
from users.models import CustomUser

def index(request):
    diary = Diary.objects.all().order_by("date").reverse()
    params = {
        'diaries_list': diary,
    }
    return render(request, 'diaries/index.html', params)

def create(request):
    if (request.method == 'POST'):
        lesson = LessonForm(request.POST)
        lesson.save()
        return redirect(to='/lessons')

    teacher = CustomUser.objects.get(id=request.user.id)
    
    params = {
        'form': DiaryForm(initial={'teacher_id': teacher}),
    }
    return render(request, 'diaries/create.html', params)

def detail(request, diary_id):
    diary = Diary.objects.get(pk=diary_id)
    params = {
        'diary': diary,
    }
    return render(request, 'diaries/detail.html', params)
