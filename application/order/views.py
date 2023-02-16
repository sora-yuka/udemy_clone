from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from application.order.permissions import IsOrderOwner
from django.contrib.auth import get_user_model
from application.course.models import Course

from application.order.serializers import (
    OrderSerializer, Order, ArchiveSerializer, Archive
)

user = get_user_model()

class OrderModelViewSet(
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    GenericViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsOrderOwner]
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    print(user)
    print(Course)
    

class ArchiveModelViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, 
    GenericViewSet):
    
    serializer_class = ArchiveSerializer
    queryset = Archive.objects.all()
    permission_classes = [IsOrderOwner]