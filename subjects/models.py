from django.db import models

class Subject(models.Model):
    name = models.CharField(("科目名"), max_length=50)
    COLOR_CHOICES = (
            ('danger','red'),
            ('primary','blue'),
            ('warning','yellow'),
            ('success','green'),
            ('secondary','gray'),
            ('dark','black'),
            ('light','white'),
        )
    color = models.CharField(("色"), max_length=20, choices=COLOR_CHOICES)

    def __str__(self):
        return self.name
