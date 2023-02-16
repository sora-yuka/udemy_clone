from django.db import transaction
from rest_framework import serializers
from django.contrib.auth import get_user_model
from application.feedback.serializers import CommentSerializer
from application.products.models import (
    Product, ProductFile, ProductItem, Category
)

user = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(source="owner.full_name", required=False)
    
    class Meta:
        model = Product
        fields = [
            "id", "owner", "title", "sub_title", "description", "language",
            "level", "category", "price", "created_at", "updated_at"
        ]
        
    @transaction.atomic
    def create(self, validated_data):
        product_data = {
            "owner": validated_data.get("owner"),
            "title": validated_data["title"],
            "sub_title": validated_data.pop("sub_title"),
            "description": validated_data["description"],
            "language": validated_data.pop("language"),
            "level": validated_data.pop("level"),
            "category": validated_data.pop("category"),
            "price": validated_data.pop("price"),
            "created_at": validated_data.get("created_at"),
            "updated_at": validated_data.get("updated_at"),
        }
        
        product = Product.objects.create(**product_data)
        
        product_item_data = {
            "title": validated_data["title"],
            "description": validated_data.get("description"),
            "course_id": product.id,
        }

        product_item = ProductItem.objects.create(**product_item_data)
        product.product_item = product_item
        
        archive_data = {
            "course_id": product.id,
            "user_id": self.context["request"].user.id
        }

        
        product_item_file_data = {
            "course_item_id": product_item,
            # "course": "example course"
        }
        
        product_item_file = ProductFile.objects.create(**product_item_file_data)
        product_item.product_item_file = product_item_file
        
        product.save()
        product_item.save()
        product_item_file.save()
        
        return product
        
    
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"