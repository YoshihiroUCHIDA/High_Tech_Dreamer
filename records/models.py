from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
# class Student(models.Model):
#     name = models.CharField(_("生徒名"), max_length=50)

# class CustomUser(models.Model):
#     name = models.CharField(_("氏名"), max_length=50)

class Records(models.Model):
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    SUBJECT_CHOICES=(
        ('国語','国語'),
        ('数学','数学'),
        ('理科','理科'),
        ('社会','社会'),
        ('英語','英語'),
    )
    TYPE_CHOICES=(
        ('定期','定期'),
        ('模試','模試'),
    )
    day = models.DateField(_("年月日"),null=True)
    type=models.CharField(_("定期or模試"), max_length=20, choices=TYPE_CHOICES)
    subject=models.CharField(_("科目選択"), max_length=20, choices=SUBJECT_CHOICES)
    score=models.FloatField(_("点数"))
    averagescore=models.FloatField(_("平均点"))



