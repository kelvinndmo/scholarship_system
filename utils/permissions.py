from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    """Allow ReadOnly permissions if the request is a safe method"""

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.role == 'ST'


class IsSponsor(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        print(user.role)
        return user.is_authenticated and user.role == 'SP'


class IsApplicant(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.role == 'AP'
