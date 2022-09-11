from django.urls import path
from . import views

app_name = 'jukus'

urlpatterns = [
    path('',views.dashboard, name='dashboard')
]
