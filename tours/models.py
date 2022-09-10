from django.db import models
from django.urls import reverse

class Hotel(models.Model):
    name = models.CharField(max_length=60)
    rating = models.IntegerField()
    year = models.IntegerField(default=2000)
    capacity = models.IntegerField(null=True)


    def __str__(self):
        return f'{self.name} - {self.rating} star'

    def get_url(self):
        return reverse('hotel-detail', args=[self.id])
