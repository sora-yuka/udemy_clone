from django.urls import path, include
from rest_framework.routers import DefaultRouter
from application.feedback.views import (
    RatingAPIView, CommentAPIView, LikeCommentAPIView
)

router = DefaultRouter()
router.register("comment", CommentAPIView)

urlpatterns = [
    path("rate/", RatingAPIView.as_view(), name="rate"),
    path("like/", LikeCommentAPIView.as_view(), name="like"),
    path("", include(router.urls))
]
