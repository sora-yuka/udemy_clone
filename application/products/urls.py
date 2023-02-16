from django.urls import path, include
from rest_framework.routers import DefaultRouter
from application.products.views import (
    ProductModelViewSet, CategoryModelViewSet, ArchiveModelViewSet
)

router = DefaultRouter()
router.register("archive", ArchiveModelViewSet)
router.register("category", CategoryModelViewSet)
router.register("", ProductModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]