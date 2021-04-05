from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, respect, view, obj):
        return obj.owner == request.user