from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=60)
    rating = models.IntegerField()
    year = models.IntegerField(default=2000)
    size = models.IntegerField(null=True)


    def __str__(self):
        return f'{self.name} {self.rating}'
