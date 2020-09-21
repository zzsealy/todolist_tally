from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    prepare_finish_time = models.DateTimeField('预计完成时间',max_length=64)
    finished_time = models.DateTimeField('实际完成时间',max_length=64, blank=True, null=True)