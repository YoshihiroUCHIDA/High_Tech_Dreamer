from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:user_id>/',views.detail, name='detail'),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('index/',views.IndexView.as_view(), name="index")
]
