from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True, blank=True)
    price = models.IntegerField(default=10)
    requirement = models.IntegerField(default=0)
    grade = models.CharField(max_length=50, default='copper')


