from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.

class User(AbstractUser):
    pass
