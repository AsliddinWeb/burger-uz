from rest_framework import serializers

from .models import Customer

class CustomerSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    security_code = serializers.CharField()

class CustomerFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields = ['name', 'tg_id', 'phone_number', 'delivery_address']
        fields = "__all__"