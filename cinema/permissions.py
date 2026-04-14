from rest_framework import permissions


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE":
            return False

        return bool(
            (
                request.method in permissions.SAFE_METHODS
                and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return False

        return bool(
            (
                request.method in permissions.SAFE_METHODS
                and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )

