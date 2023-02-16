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
#?  -->  при написании source важно обратить внимание как написан related_name в модельках.
    
    class Meta:
        model = Comment
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation["likes"] = instance.like_comment.filter(like=True).count()
        return representation

class LikeCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    
    class Meta:
        model = LikeComment
        fields = "__all__"
