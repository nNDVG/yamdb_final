from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_staff or request.user.is_superuser


class IsSuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            not (not request.user.is_superuser and not request.user.is_staff and not (request.user.role == 'admin'))
        )
