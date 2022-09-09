from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=60)
    rating = models.IntegerField()
