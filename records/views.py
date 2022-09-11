from django.shortcuts import render
from django.http import HttpResponse
from .models import Records
# Create your views here.


def index(request):
    data=Records.objects.all()
    params={'data':data}
    return render(request,'list.html',params)

def detail(request,records_id):
    data=Records.objects.filter(pk=records_id)
    params={'data':data}
    return render(request,'detail.html',params)
