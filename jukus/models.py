from django.db import models

class Juku(models.Model):
    name = models.CharField(("塾名"), max_length=50)
    news = models.CharField(("お知らせ"), max_length=200,null=True)

    def __str__(self):
        return self.name
