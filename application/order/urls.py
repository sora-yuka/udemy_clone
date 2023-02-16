from django.urls import path, include
from rest_framework.routers import DefaultRouter
from application.order.views import OrderModelViewSet, ArchiveModelViewSet

router = DefaultRouter()
router.register("archive", ArchiveModelViewSet)
router.register("", OrderModelViewSet)

urlpatterns = [
    path("", include(router.urls))
]
