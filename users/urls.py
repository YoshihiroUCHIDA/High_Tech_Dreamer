from django.urls import path
from . import views
from records import views as records_views

app_name = 'users'

urlpatterns = [
    path('<int:user_id>/',views.detail, name='detail'),
    path('<int:user_id>/records/',records_views.index, name='records_detail'),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('index/',views.index, name="index"),
    path('edit/<int:user_id>/',views.edit,name="edit")
    path('teacher_index/',views.teacher_index, name="teacher_index"),
    path('follow/<int:user_id>/',views.follow, name="follow")
]
