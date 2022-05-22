from django.db import models

# Create your models here.
class Invoice(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TimeField(blank=True,default='')
    total = models.DecimalField(max_digits=7, decimal_places=2)
    paid = models.DecimalField(max_digits=7, decimal_places=2)

class Items(models.Model):
    product = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    qty = models.IntegerField(default=1)
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, default='')
    total = models.DecimalField(max_digits=7, decimal_places=2)
