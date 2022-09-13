from django.shortcuts import render

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
