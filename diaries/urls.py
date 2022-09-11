from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:diary_id>/', views.detail, name='detail')
]
