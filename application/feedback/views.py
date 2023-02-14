from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from application.feedback.models import (
    Comment, Rating, LikeComment
)
from application.feedback.serializers import (
    CommentSerializer, RatingSerializer, LikeCommentSerializer
)
from rest_framework.generics import (
    CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
)
from application.feedback.permissions import IsFeedbackOwner


class RatingAPIView(CreateAPIView, ListAPIView, DestroyAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    permission_classes = [IsFeedbackOwner]
    
class CommentAPIView(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsFeedbackOwner]
    

class LikeCommentAPIView(CreateAPIView, ListAPIView, DestroyAPIView):
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()
    permission_classes = [IsFeedbackOwner]