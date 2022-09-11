from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from accounts.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from . import forms

# --------------------------------------------------
class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = 'accounts/login.html'

# --------------------------------------------------
class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'

# --------------------------------------------------
class IndexView(TemplateView):
    template_name = 'accounts/index.html'
    
# --------------------------------------------------
# ユーザ作成
class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/create.html'
    success_url = reverse_lazy('login')