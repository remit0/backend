from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ProductManager(models.Manager):

    def get_by_natural_key(self, name, year, type, store):
        return self.get(name=name, year=year, type=type, store=store)


class Product(models.Model):

    class Meta:
        unique_together = [['name', 'year', 'type', 'store']]

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

    def natural_key(self):
        return self.name, self.year, self.type, self.store


class Rating(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=-1, validators=[MinValueValidator(-1), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.user.id}): {self.product.name} :{self.rating}"

    def as_dict(self):
        return {
            'user': self.user.id,
            'product': self.product.id,
            'rating': self.rating,
            'date': str(self.date.date())
        }
