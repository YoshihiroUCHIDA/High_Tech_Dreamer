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

class Record(models.Model):
    name = models.CharField(_("テスト名"), max_length=50)
    date = models.DateField(_("年月日"),null=True)
    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    TYPE_CHOICES=(
        ('定期','定期'),
        ('模試','模試'),
    )
    type = models.CharField(_("定期or模試"), max_length=20, choices=TYPE_CHOICES)

    score_japanese = models.FloatField(_("国語の点数"))
    score_math     = models.FloatField(_("数学の点数"))
    score_english  = models.FloatField(_("英語の点数"))
    score_sience   = models.FloatField(_("理科の点数"))
    score_social   = models.FloatField(_("社会の点数"))

    average_japanese = models.FloatField(_("国語の平均点"))
    average_math     = models.FloatField(_("数学の平均点"))
    average_english  = models.FloatField(_("英語の平均点"))
    average_sience   = models.FloatField(_("理科の平均点"))
    average_social   = models.FloatField(_("社会の平均点"))

    diviation_japanese = models.FloatField(_("国語の偏差値"))
    diviation_math     = models.FloatField(_("数学の偏差値"))
    diviation_english  = models.FloatField(_("英語の偏差値"))
    diviation_sience   = models.FloatField(_("理科の偏差値"))
    diviation_social   = models.FloatField(_("社会の偏差値"))

    def __str__(self):
        return self.name
