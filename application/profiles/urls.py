from django.urls import path, include
from rest_framework.routers import DefaultRouter
from application.profiles.views import ProfileModelViewSet

router = DefaultRouter()
router.register("", ProfileModelViewSet)

urlpatterns = [
    path("", include(router.urls))
]
