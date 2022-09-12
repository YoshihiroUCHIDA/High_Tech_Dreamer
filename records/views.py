from django.shortcuts import render
from django.http import HttpResponse
from .models import Record
# Create your views here.


def index(request, user_id):
    records = Record.objects.filter(student_id=user_id)
    user = request.user
    params={
            'records_list' : records
        }
    return render(request,'records/index.html',params)

def detail(request,record_id):
    data=Record.objects.filter(pk=record_id)
    params={'data':data}
    return render(request,'records/detail.html',params)
