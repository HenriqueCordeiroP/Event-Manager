from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsEventCreator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve']:
            return True
        
        if obj.user == request.user:
            return True
        
        raise PermissionDenied("You do not have permission to modify this event.")