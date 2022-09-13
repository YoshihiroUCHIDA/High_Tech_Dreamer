from django.shortcuts import render
from users.models import CustomUser
from .models import Lesson

def index(request):
    lessons = Lesson.objects.all().order_by("date").reverse()
    params = {
        'lessons': lessons,
    }
    return render(request, 'lessons/index.html', params)

def create(request):
    if (request.method == 'POST'):
        lesson = LessonForm(request.POST)
        lesson.save()
        return redirect(to='/lessons')

    teacher = CustomUser.objects.get(id=request.user.id)
    
    params = {
        'form': DiaryForm(initial={'teacher_id': teacher}),
    }
    return render(request, 'lessons/create.html', params)

def detail(request, diary_id):
    diary = Diary.objects.get(pk=diary_id)
    params = {
        'diary': diary,
    }
    return render(request, 'lessons/detail.html', params)
