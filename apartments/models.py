from unicodedata import name
from django.db import models

# Create your models here.


class Apartment(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bathrooms = models.IntegerField()
    num_bedrooms = models.IntegerField()
    square_footage = models.IntegerField()
    adress = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.title
