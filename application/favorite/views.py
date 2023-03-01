from django.shortcuts import render
from application.favorite.models import Favorite
from application.favorite.serializers import FavoriteSerializer
from application.favorite.permissions import IsFavoriteOwner
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
)


class FavoriteModelViewSet(ListModelMixin,
                           RetrieveModelMixin,
                           CreateModelMixin,
                           DestroyModelMixin,
                           GenericViewSet):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
    permission_classes = [IsFavoriteOwner]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    