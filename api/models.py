from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Product(models.Model):

    type_choices = [
        ('-', '-'),
        ('BEER', 'Beer'),
        ('WINE', 'Wine'),
        ('RUM', 'Rum'),
        ('TEQUILA', 'Tequila'),
        ('VODKA', 'Vodka'),
        ('WHISKY', 'Whisky'),
    ]
    store_choices = [
        ('-', '-'),
        ('CARREFOUR', 'Carrefour'),
        ('MONOPRIX', 'Monoprix'),
        ('FRANPRIX', 'Franprix'),
        ('LECLERC', 'Leclerc'),
        ('AUCHAN', 'Auchan'),
    ]
    name = models.CharField(max_length=500, default="-")
    year = models.IntegerField(default=-1)
    vol = models.FloatField(default=-1, validators=[MinValueValidator(-1), MaxValueValidator(90)])
    type = models.CharField(max_length=100, default="-", choices=type_choices)
    store = models.CharField(max_length=100, default="-", choices=store_choices)

    def __str__(self):
        return f"{self.name}"


class Rating(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=-1, validators=[MinValueValidator(-1), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} : {self.product.name} :{self.rating}"
