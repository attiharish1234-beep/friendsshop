from django.db import models

class Order(models.Model):
    product = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    payment_status = models.CharField(max_length=20, default="Pending")
    txn_id = models.CharField(max_length=100, null=True, blank=True)