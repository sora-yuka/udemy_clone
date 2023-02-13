from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from application.order.serializers import OrderSerializer, Order


class OrderModelViewSet(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    GenericViewSet
):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()