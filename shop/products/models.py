from django.db import models


class Product(models.Model):
    """
    Product model in database
    """

    title = models.CharField(max_length=50)
    image = models.ImageField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
