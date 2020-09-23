from django.db import models

# Create your models here.


class Todo(models.Model):
    content = models.TextField(blank=True, null=True)
    # 都用CharField吧
    prepare_finish_time = models.CharField('预计完成时间',max_length=64, blank=True, null=True)
    finished_time = models.CharField('实际完成时间',max_length=64, blank=True, null=True)