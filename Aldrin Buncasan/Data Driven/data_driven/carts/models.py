from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    STATUS_IN_CART = 'in_cart'
    STATUS_PAID = 'paid'
    ORDER_STATUS = (
        (STATUS_IN_CART, 'In Cart'),
        (STATUS_PAID, 'Paid')
    )
 
    status = models.CharField(max_length=10, default=STATUS_IN_CART, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.status
