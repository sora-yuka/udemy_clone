from rest_framework import serializers
from application.order.models import Order, Archive


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = "__all__"
        
        
class ArchiveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Archive
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation["user"] = instance.user.email
        return representation