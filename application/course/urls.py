from django.urls import path, include
from rest_framework.routers import DefaultRouter
from application.course.views import (
    CourseModelViewSet, CategoryModelViewSet
)

router = DefaultRouter()
router.register("category", CategoryModelViewSet)
router.register("", CourseModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]