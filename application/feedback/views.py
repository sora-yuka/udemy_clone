from django.shortcuts import render
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


class RatingAPIView(CreateAPIView, ListAPIView):
    serializer_class = RatingSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsFeedbackOwner]