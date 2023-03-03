from rest_framework import serializers
from application.feedback.models import Comment
from application.feedback.serializers import CommentSerializer
from rest_framework.decorators import action
from django.db.models import Avg
from application.course.models import (
    Course, CourseFile, CourseItem,
)


class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(source="owner.email", required=False)
    description = serializers.CharField(min_length=200)
    
    class Meta:
        model = Course
        fields = [
            "id", "owner", "title", "sub_title", "category", "sub_category", "secondery_category",
            "description", "language", "level", "price", "image", "video", "created_at", "updated_at",
        ]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        comment = Comment.objects.filter(courses=instance.id)
        
        representation["rating"] = instance.ratings.all().aggregate(Avg("rating"))["rating__avg"]
        representation["comment"] = CommentSerializer(comment, many=True).data
        return representation
        
        
class CourseFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseFile
        fields = "__all__"
        
        
class CourseItemSerializer(serializers.ModelSerializer):
    file = CourseFileSerializer(many=True, read_only=True)
    course_file = serializers.ListField(
        child=serializers.FileField(max_length=None, allow_empty_file=False, use_url=False),
        min_length=5,
        max_length=None,
        write_only=True, 
    )
    
    class Meta:
        model = CourseItem
        fields = "__all__"
        
    
    def create(self, validated_data):
        files_data = validated_data.pop("course_file")
        course_file = CourseItem.objects.create(**validated_data)
        for file in files_data:
            CourseFile.objects.create(course_file=course_file, file=file)
        
        return course_file