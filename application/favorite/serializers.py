import statistics
from rest_framework import serializers
from django.db.models import Avg
from application.favorite.models import Favorite
from application.feedback.models import Rating, Comment
from application.feedback.serializers import RatingSerializer
from rest_framework.response import Response


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email", required=False)
    
    class Meta:
        model = Favorite
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        ratings = RatingSerializer(instance.course.ratings, many=True).data
        
        representation["Preview"] = str(instance.course.image)
        representation["Title"] = instance.course.title
        representation["Teacher"] = instance.course.owner.first_name
        try:
            representation["Ratings"] = statistics.mean([rating["rating"] for rating in ratings])
        except:
            pass
        representation["Couments"] = Comment.objects.filter(courses_id=instance.course.id).count()
        representation["Price"] = instance.course.price
        
        return representation
    