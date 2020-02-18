from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Product(models.Model):
    # required
    name = models.CharField(max_length=500)
    # optional
    year = models.IntegerField(null=True, default=None)
    vol = models.FloatField(max_length=2, null=True, default=None,
                            validators=[MinValueValidator(0), MaxValueValidator(90)])
    type = models.CharField(max_length=100, null=True, default=None)
    store = models.CharField(max_length=100, null=True, default=None)

    def __str__(self):
        return f"{self.name}"

    @staticmethod
    def get_attributes():
        return ["name", "year", "vol", "type", "store"]


class Rating(models.Model):
    # required
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    # autofilled
    date = models.DateTimeField(auto_now_add=True)
    # optional
    comment = models.CharField(max_length=500, null=True, default=None)

    def __str__(self):
        return f"{self.product.name}: {self.value} ({self.user.username})"

    @staticmethod
    def get_attributes():
        return ["user", "product", "value", "date", "comment"]
