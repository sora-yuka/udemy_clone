from rest_framework import serializers
from django.shortcuts import get_object_or_404
from application.favorite.models import Favorite
from application.feedback.models import Rating, Comment
from application.feedback.serializers import RatingSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email", required=False)
    
    class Meta:
        model = Favorite
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation["Preview"] = str(instance.course.image)
        representation["Title"] = instance.course.title
        representation["Teacher"] = instance.course.owner.first_name
        # representation["Ratings"] = (RatingSerializer(Rating.objects.all()).data)
        representation["Ratings"] = RatingSerializer(Rating.objects.get(courses_id=instance.course.id)).data
        representation["Couments"] = Comment.objects.filter(courses_id=instance.course.id).count()
        
        return representation