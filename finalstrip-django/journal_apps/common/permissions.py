from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = (
        "You do not have permission to update or delete."
    )

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return obj.user == request.user


class AllowedToView(permissions.BasePermission):
    message = (
        "You do not have permission to view."
    )

    def has_object_permission(self, request, view, obj):
        
        requester = request.user
        owner = obj.user
        
        if request.user.is_superuser: return True
        if owner == requester: return True

        permission_level = obj.shareable

        if permission_level == "friends":
            pass

        return False
    