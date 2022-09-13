from django.db import models
from users.models import CustomUser
from diaries.models import Diary
from subjects.models import Subject
from django.utils.translation import gettext_lazy as _

class Lesson(models.Model):
    date = models.DateField(_("日時"))
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    diary = models.ForeignKey(Diary,Diary,null=True)
    users = models.ManyToManyField(CustomUser,null=True)

    def __str__(self):
        return self.date
