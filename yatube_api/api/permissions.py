from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Права для запроса доступны только автору, иначе доступ запрещен."""
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
