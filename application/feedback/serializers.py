from rest_framework import serializers
from application.feedback.models import Rating, Comment, LikeComment
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
#?  -->  при написании source важно обратить внимание как написан related_name в модельках.

    class Meta:
        model = Comment
        fields = "__all__"


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation["likes"] = instance.likes_comment.filter(like=True).count()
        representation["dislikes"] = instance.likes_comment.filter(dislike=True).count()
#?      при написании representation важно обратить внимание на наличие related_name у связываемого объекта.
        return representation
    

class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=10)
    
    class Meta:
        model = Rating
        fields = ["rating"]