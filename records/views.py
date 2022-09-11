from django.shortcuts import render
from django.http import HttpResponse
from .models import Record
# Create your views here.


def index(request):
    data=Record.objects.all()
    params={'data':data}
    return render(request,'list.html',params)

def detail(request,record_id):
    data=Record.objects.filter(pk=record_id)
    params={'data':data}
    return render(request,'detail.html',params)
