from django.db import models
from todolist_tally.apps.account.models import User
# Create your models here.user

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    category = models.TextField(blank=True, null = True)
    money = models.CharField(max_length=128)


