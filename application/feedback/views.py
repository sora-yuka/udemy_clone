from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from application.feedback.models import (
    Comment, Rating, LikeComment
)
from application.feedback.serializers import (
    CommentSerializer, RatingSerializer
)
from rest_framework.generics import (
    CreateAPIView, ListAPIView, UpdateAPIView
)
from application.feedback.permissions import IsFeedbackOwner

 
class CommentAPIView(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsFeedbackOwner]
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    @action(detail=True, methods=["POST"])
    def like(self, request, pk, *args, **kwargs):
        like_obj, created = LikeComment.objects.get_or_create(
            user=request.user,
            course_comment_id=pk,
        )
        like_obj.like = not like_obj.like
        like_obj.save()
        status = "liked" if like_obj.like else "unliked"
        return Response(
            {"status": status}
        )
    
    @action(detail=True, methods=["POST"])
    def dislike(self, request, pk, *args, **kwargs):
        dislike_obj, created = LikeComment.objects.get_or_create(
            user=request.user,
            course_comment_id=pk,
        )
        dislike_obj.dislike = not dislike_obj.dislike 
        dislike_obj.save()
        status = "disliked" if dislike_obj.dislike else "undisliked"
        return Response(
            {"status": status}
        )