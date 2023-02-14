from rest_framework.permissions import BasePermission

class IsProfileOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHOD:
            return True
        return request.user.is_authenticated and reqeust.user == obj.owner