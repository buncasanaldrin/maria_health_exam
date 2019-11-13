from rest_framework import serializers
from .models import Cart
from order_products.models import OrderProduct

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']

class CartSerializer(serializers.ModelSerializer):

    cart = OrderProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'status', 'cart']

    def validate(self, data):
        
        if data['status'] == 'in_cart':
            raise serializers.ValidationError({'status': ['Changing or updating it back to in_cart status is not allowed']})

        return data