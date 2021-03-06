from django.db import models
from todolist_tally.apps.account.models import User
# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    # 都用CharField吧
    prepare_finish_time = models.CharField('预计完成时间', max_length=64, blank=True, null=True)
    finished_time = models.CharField('实际完成时间', max_length=64, blank=True, null=True)
    done = models.BooleanField('完成', default=False)
