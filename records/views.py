from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Record
from django.core import serializers
import json


def index(request, user_id):
    records = Record.objects.filter(student_id=user_id)
    records_teiki = Record.objects.filter(student_id=user_id).filter(type="定期")
    records_moshi = Record.objects.filter(student_id=user_id).filter(type="模試")
    records_teiki_json = json.dumps(serializers.serialize("json", records_teiki))
    records_moshi_json = json.dumps(serializers.serialize("json", records_moshi))

    params = {
            'records' : records,
            'records_teiki' : records_teiki,
            'records_moshi' : records_moshi,
            'records_teiki_json' : json.dumps(records_teiki_json),
            'records_moshi_json' : json.dumps(records_moshi_json),
        }
    return render(request,'records/index.html',params)

def detail(request,record_id):
    data = Record.objects.filter(pk=record_id)
    params = {'data' : data }
    return render(request,'records/detail.html',params)


def chart(request):
    records = list(Record.objects.filter(student_id = request.user.id).values())
    data = { 'records' : records }
    return JsonResponse(data)
