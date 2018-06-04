
from datetime import datetime
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    images = models.ImageField(height_field=None, width_field=None, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, default="UAH")
    description = models.TextField()
    date_of_publishing = models.DateField(blank=True, default=datetime.now)
    date_of_adding = models.DateField(auto_now=True)