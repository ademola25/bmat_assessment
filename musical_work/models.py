from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class MusicalWork(models.Model):
    title = models.TextField(max_length=40)
    contributors = ArrayField(models.TextField(max_length=40))
    iswc = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.title