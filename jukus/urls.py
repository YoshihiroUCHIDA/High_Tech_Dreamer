from django.urls import path
from . import views


urlpatterns = [
    path('',views.top, name='top'),
    path('<int:juku_id>/',views.detail, name='detail')
]
