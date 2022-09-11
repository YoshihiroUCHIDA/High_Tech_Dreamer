from django.urls import path
from . import views

app_name = 'subjects'

urlpatterns = [
    path('' ,views.index, name='index'),
]
