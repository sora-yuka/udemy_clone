from django.shortcuts import render
from application.products.models import Product, Category, Archive
from application.feedback.serializers import CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from application.products.permissions import (
    IsProductOwnerOrReadOnly, IsArchiveOwner
)
from application.products.serializers import (
    ProductSerializer, ArchiveSerializer, CategorySerializer
)


class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsProductOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "owner"]
    search_fields = ["title"]
    order_fields = ["price"]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        return super().get_queryset()


class ArchiveModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = ArchiveSerializer
    queryset = Archive.objects.all()
    permission_classes = [IsArchiveOwner]
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # search_fields = ["title"]
    
    
class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
