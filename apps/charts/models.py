from django.db import models
from django.contrib.auth.models import User


class ClientChartsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_constraint=False)
    client = models.CharField('客户端号', max_length=255)
    points = models.PositiveIntegerField('分数', max_length=7)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name = '客户端分数表'
        db_table = 'client_points'