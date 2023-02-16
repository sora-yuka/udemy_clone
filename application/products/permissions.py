from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProductOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)
    

class IsArchiveOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            print(f"Checking permissions for user {request.user} on object {obj}")
            return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)
        return False