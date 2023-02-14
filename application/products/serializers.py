from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(source="owner.full_name", required=False)
    
    class Meta:
        model = Product
        fields = "__all__"
        
        
        def create(self, request):
            request = self.context.get("request")
            product = Product.objects.create(**validated_data)
            return product
        
        # def to_representation(self, isinstance):
        #     representation = super().to_representation(instance)
            
        #     representation["comment"] = instance.commtn.filter(comment=True).count()
        #     return representation
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"