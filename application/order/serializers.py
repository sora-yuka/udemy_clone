from django.db import transaction
from rest_framework import serializers
from application.order.models import Order, Archive
from django.contrib.auth import get_user_model
from application.course.models import Course

user = get_user_model()


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")
    
    class Meta:
        model = Order
        fields = "__all__"
        
        
    @transaction.atomic
    def create(self, validated_data):
        order_data = {
            "owner_id": self.context["request"].user.id,
            "course_id": validated_data.get("course").id,
        }
        
        order = Order.objects.create(**order_data)
        
        archive_data = {
            "owner_id": self.context["request"].user.id,
            "course_id": validated_data.get("course").id,
        }
        
        archive = Archive.objects.create(**archive_data)
        order.archive = archive
        
        order.save()
        archive.save()
        
        return order
        
        
class ArchiveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Archive
        fields = "__all__"
        

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation["user"] = instance.user.email
        return representation
