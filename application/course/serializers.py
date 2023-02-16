from django.db import transaction
from rest_framework import serializers
from application.feedback.serializers import CommentSerializer
from application.course.models import (
    Course, CourseFile, CourseItem, Category
)


class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(source="owner.full_name", required=False)
    
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
        
        course_item_file_data = {
            "course_item_id": course_item,
            # "course": "example course"
        }
        
        course_item_file = CourseFile.objects.create(**course_item_file_data)
        course_item.course_item_file = course_item_file
        
        course.save()
        course_item.save()
        course_item_file.save()
        
        return course
        
    
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"