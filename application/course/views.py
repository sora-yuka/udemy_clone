from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin, DestroyModelMixin
)
from rest_framework.filters import SearchFilter, OrderingFilter
from application.feedback.models import Rating
from application.course.models import Course, CourseFile, CourseItem
from application.course.serializers import (
    CourseSerializer, CourseFileSerializer, CourseItemSerializer
)
from application.feedback.serializers import CommentSerializer, RatingSerializer
from application.course.permissions import IsCourseOwnerOrReadOnly


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
    
    @action(detail=True, methods=["POST"])
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, created = Rating.objects.get_or_create(
            user=request.user,
            courses_id=pk,
        )
        rating_obj.rating = request.data["rating"]
        rating_obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
    
    
class CourseItemModelViewSet(ModelViewSet):
    serializer_class = CourseItemSerializer
    queryset = CourseItem.objects.all()


# class CourseFileModelViewSet(ListModelMixin,
#                         CreateModelMixin, 
#                         DestroyModelMixin,
#                         GenericViewSet):
#     serializer_class = CourseFileSerializer
#     queryset = CourseFile.objects.all()