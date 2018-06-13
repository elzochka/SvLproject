
from datetime import datetime
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  #changed Product object into Product name in django admin
        return self.name

    images = models.ImageField(height_field=None, width_field=None, max_length=100, help_text="You can download up to 5 pictures")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, default="UAH", choices=[('UAH', 'UAH'), ('USD', 'USD'), ('EURO', 'EURO')])
    description = models.TextField()
    date_of_publishing = models.DateField(blank=True, default=datetime.now)
    date_of_adding = models.DateField(auto_now=True)
    details = models.TextField()
    about_brand = models.TextField()
    sizing = models.TextField()
    shipping = models.TextField()

class Image(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(height_field=None, width_field=None, max_length=100, help_text="You can download up to 5 pictures")


