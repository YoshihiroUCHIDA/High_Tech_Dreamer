from django.db import models

class subject(models.Model):
    name = models.CharField(("科目名"), max_length=50)