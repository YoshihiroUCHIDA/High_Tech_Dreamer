from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import CustomUser

# --------------------------------------------------
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
        
# --------------------------------------------------
# Eメールを用いた認証の実装
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = {'email', "name", "school", "birthday", 'job', 'juku','bio','profile_image','subjects'}
        widgets = {
            'birthday': forms.SelectDateWidget
        }
