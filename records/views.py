from django.shortcuts import render
from django.http import HttpResponse
from .models import Record
from django.core import serializers
import json


def index(request, user_id):
    user = request.user
    records = Record.objects.filter(student_id=user_id)
    records_json = json.dumps(serializers.serialize("json", records))
    params={
            'records' : records,
            'records_json' : json.dumps(records_json)
        }
    return render(request,'records/index.html',params)

def detail(request,record_id):
    data=Record.objects.filter(pk=record_id)
    params={'data':data}
    return render(request,'records/detail.html',params)
