from rest_framework import serializers
from application.products.models import Product, Category
from application.feedback.serializers import CommentSerializer


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(source="owner.full_name", required=False)
    
    class Meta:
        model = Product
        # fields = "__all__"
        
        
        def create(self, request):
            request = self.context.get("request")
            product = Product.objects.create(**validated_data)
            return product
    
    
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"