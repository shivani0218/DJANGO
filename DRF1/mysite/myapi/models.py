from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, default='')
    brand = models.CharField(max_length=255, default='Brand')
    product_max_price = models.CharField(max_length=255, default='')
    product_discount_price = models.CharField(max_length=255, default='')
    product_description = models.TextField(default='')
    product_long_description = models.TextField()
    in_stock_total = models.IntegerField(default=1)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.ForeignKey(Product , on_delete=models.DO_NOTHING)
    purchase_price = models.CharField(max_length=255)
    discount_amt = models.CharField(max_length=255)
    product_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)