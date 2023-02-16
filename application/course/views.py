from django.shortcuts import render
from rest_framework import mixins
from rest_framework.response import Response
from application.course.models import Course, Category
from application.feedback.serializers import CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from application.course.permissions import IsCourseOwnerOrReadOnly
from application.course.serializers import (
    CourseSerializer, CategorySerializer
)


class CourseModelViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsCourseOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "owner"]
    search_fields = ["title"]
    order_fields = ["price"]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        return super().get_queryset()


class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]