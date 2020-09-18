from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=256)

    def set_password(self):
