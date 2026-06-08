from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    payment_status = models.CharField(max_length=20, default="Pending")
    txn_id = models.CharField(max_length=100, null=True, blank=True)