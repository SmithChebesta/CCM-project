from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Code(models.Model):
    exp = models.DateTimeField()
    point = models.FloatField()
    code = models.TextField(primary_key=True)
    used_by = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True)
    used = models.BooleanField()
    used_at = models.DateTimeField(default=None, null=True)

    atvname = models.ForeignKey(
        'Activity',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.code} from {self.atvname}'


class Activity(models.Model):
    atvname = models.TextField(primary_key=True)
    date = models.DateTimeField()
    status = models.BooleanField()
    place = models.TextField()

    def __str__(self):
        return self.atvname
