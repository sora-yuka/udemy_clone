from rest_framework import serializers
from application.feedback.models import Rating, Comment, LikeComment
from django.contrib.auth import get_user_model

User = get_user_model()


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    
    class Meta:
        model = Rating
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    
    class Meta:
        model = Comment
        fields = "__all__"


class LikeCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    
    class Meta:
        model = LikeComment
        fields = "__all__"