from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=500)
    year = models.IntegerField()
    vol = models.FloatField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
