from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from carts.models import Cart

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, related_name='cart', on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
