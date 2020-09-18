from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    prepare_finish_time = models.TimeField()
    finished_time = models.TimeField()