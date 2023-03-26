from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    # product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='product')
    product_quantity = models.IntegerField(default=1)
    product_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name_plural = 'Products'


class Address(models.Model):
    line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.city
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    profile_image = models.ImageField()
    contact_number = models.BigIntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.full_name


class CartDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField()

ORDER_STATUS = [
    ('order place', 'order place'),
    ('packing', 'packing'),
    ('in transit', 'in transit'),
    ('out for delivery', 'out for delivery'),
    ('delivered', 'delivered'), 
]

class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()
    quantity = models.IntegerField()
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS)