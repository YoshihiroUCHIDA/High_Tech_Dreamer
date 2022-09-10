from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser

# Create your views here.

def index(request):
    return render(request, 'index.html')

def detail(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    name = user.name
    return HttpResponse(name)
