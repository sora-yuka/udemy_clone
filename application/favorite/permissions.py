from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsFavoriteOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (obj.user == request.user or request.user.is_staff)