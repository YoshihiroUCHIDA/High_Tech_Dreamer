from django.urls import path
from . import views


urlpatterns = [
    #path('',views.detail, name='top'),
    path('<int:juku_id>/',views.dashboard, name='dashboard')
]
