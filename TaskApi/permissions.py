from rest_framework import permissions

# Permissions for owner or staff
class OwnerAndStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff
