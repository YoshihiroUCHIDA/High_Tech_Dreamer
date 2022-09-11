from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('<int:user_id>/',views.detail, name='detail'),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('',views.MyLoginView.as_view(), name="empty_url_login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('index/',views.index, name="index")
]
