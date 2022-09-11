from django.db import models
#from subjects.models import oo
from users.models import CustomUser
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------
# 日誌モデルの定義
class Diary(models.Model):
    range = models.CharField(_('学習範囲'), max_length=50)
    #subject_id = models.ForeignKey(oo, on_delete=models.CASCADE)
    homework = models.CharField(_('宿題'), max_length=50)
    date = models.DateTimeField(_('日付'), null=True)
    content = models.CharField(_('内容'), max_length=100)
    teacher_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teacher', to_field='id')
    student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student', to_field='id')
    remark = models.CharField(_('備考'), max_length=100)
