from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser

# Create your views here.

def index(request):
    users = CustomUser.objects.all()
    context = { 'users_list': users,}
    return render(request, 'users/index.html', context)

def detail(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    context = { 'user': user,}
    return render(request, 'users/detail.html', context)
