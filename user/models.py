from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username