from rest_framework import serializers
from .models import Hmo


class HmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hmo
        fields = '__all__'
