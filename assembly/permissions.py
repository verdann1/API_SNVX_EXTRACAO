from rest_framework import permissions


class AssemblyPermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('assembly.view_genre')

        if request.method == 'POST':
            return request.user.has_perm('assembly.add_genre')

        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('assembly.change_genre')

        if request.method == 'DELETE':
            return request.user.has_perm('assembly.delete_genre')

        return False
