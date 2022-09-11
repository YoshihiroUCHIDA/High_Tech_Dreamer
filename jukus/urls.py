from django.urls import path
from . import views

app_name = 'jukus'

urlpatterns = [
    #path('',views.detail, name='top'),
    path('<int:juku_id>/',views.dashboard, name='dashboard')
]
