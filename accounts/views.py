from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"

class IndexView(TemplateView):
    template_name = "accounts/index.html"