from django.shortcuts import render
from application.profiles.models import Profile
from application.profiles.serializers import ProfileSerializer
from application.profiles.permissions import IsProfileOwner
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileModelViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsProfileOwner]
    
    def get_queryset(self):
        return super().get_queryset()
