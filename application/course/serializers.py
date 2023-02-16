from django.db import transaction
from rest_framework import serializers
from application.feedback.models import Comment
from application.feedback.serializers import CommentSerializer
from application.course.models import (
    Course, CourseFile, CourseItem, Category
)


class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(source="owner.full_name", required=False)
    description = serializers.CharField(min_length=200)
    
    class Meta:
        model = Course
        fields = [
            "id", "owner", "title", "sub_title", "description", "language",
            "level", "category", "price", "created_at", "updated_at"
        ]
        
    @transaction.atomic
    def create(self, validated_data):
        course_data = {
            "owner": validated_data.get("owner"),
            "title": validated_data["title"],
            "sub_title": validated_data.get("sub_title"),
            "description": validated_data["description"],
            "language": validated_data.get("language"),
            "level": validated_data.get("level"),
            "category": validated_data.get("category"),
            "price": validated_data.get("price"),
            "created_at": validated_data.get("created_at"),
            "updated_at": validated_data.get("updated_at"),
        }
        
        course = Course.objects.create(**course_data)
        
        course_item_data = {
            "title": validated_data["title"],
            "description": validated_data.get("description"),
            "course_id": course.id,
        }

        course_item = CourseItem.objects.create(**course_item_data)
        course.course_item = course_item

        course.save()
        course_item.save()
        
        return course
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        comment = Comment.objects.filter(course=instance.id)
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