from rest_framework import serializers
from application.feedback.models import Comment
from application.feedback.serializers import CommentSerializer
from application.course.models import (
    Course, CourseFile, CourseItem, Category,
    SubCategory, SeconderyCategory
)


class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(source="owner.full_name", required=False)
    description = serializers.CharField(min_length=200)
    
    class Meta:
        model = Course
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        comment = Comment.objects.filter(courses=instance.id)
        comments = CommentSerializer(comment, many=True).data
        
        representation["comment"] = comments
        return representation
        
    
class CourseFileSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source="course.id")
    
    class Meta:
        model = CourseFile
        fields = "__all__"
    
    
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        

class SubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = "__all__"
        
        
class SeconderyCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SeconderyCategory
        fields = "__all__"