from rest_framework import serializers
from application.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source="user_id.email", required=False)
    
    class Meta:
        model = Profile
        fields = "__all__"
