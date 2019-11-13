from rest_framework import serializers
from .models import PaymentTerm

class PaymentTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTerm
        fields = '__all__'
