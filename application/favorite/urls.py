from django.urls import path, include
from rest_framework.routers import DefaultRouter
from application.favorite.views import FavoriteModelViewSet

router = DefaultRouter()
router.register("", FavoriteModelViewSet)

urlpatterns = [
    path("", include(router.urls))
]
