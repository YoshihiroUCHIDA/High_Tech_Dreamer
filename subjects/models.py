from django.db import models

class Subject(models.Model):
    name = models.CharField(("科目名"), max_length=50)
    
    def __str__(self):
        return self.name