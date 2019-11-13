from rest_framework import serializers

from .models import OrderProduct
from carts.models import Cart
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        cart_id = serializers.ReadOnlyField(source='cart')
        fields = ['id', 'product', 'quantity', 'cart_id']


    def create(self, data):
        
        if self.context['request'].user:
            user_id = self.context['request'].user.id
        else:
            user_id = None

        user = get_object_or_404(User, pk=user_id)

        try:
            cart = Cart.objects.get(created_by=user, status='in_cart')
        except Cart.DoesNotExist:
            cart = Cart.objects.create(created_by=user, status='in_cart')
            cart.save()

        data['cart'] = cart
        data['created_by'] = user

        try:
            order_product = OrderProduct.objects.get(product=data.get('product'), cart=data.get('cart'),)
            order_product.quantity += data.get('quantity')
            order_product.save()
        except ObjectDoesNotExist:
            order_product = OrderProduct.objects.create(**data)

  
        return order_product