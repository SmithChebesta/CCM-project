from django.db import models

# Create your models here.


class Code(models.Model):
    exp = models.DateTimeField()
    point = models.FloatField()
    used = models.BooleanField()
    code = models.TextField(primary_key=True)
    atvcode = models.ForeignKey(
        'Activity',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.code} from {self.atvcode}'


class Activity(models.Model):
    atvcode = models.TextField(primary_key=True)
    name = models.TextField()
    date = models.DateTimeField()
    status = models.BooleanField()
    place = models.TextField()

    def __str__(self):
        return self.name
