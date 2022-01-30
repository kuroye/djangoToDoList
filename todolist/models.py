from datetime import timedelta

from django.db import models
from user.models import User
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=500, null=True, blank=True)
    is_finished = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    create_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)

    class Meta:
        db_table = 'todo'

    def __str__(self):
        return f'{self.title} {self.creator.username}'
