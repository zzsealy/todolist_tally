from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    prepare_finish_time = models.CharField(max_length=64)
    finished_time = models.CharField(max_length=64)