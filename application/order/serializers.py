from rest_framework import serializers
from application.order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = "__all__"