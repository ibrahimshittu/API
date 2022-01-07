from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_obj_permission(self, obj, request, view):
        return obj.owner == request.user
