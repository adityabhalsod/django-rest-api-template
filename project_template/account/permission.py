# -*- coding: utf-8 -*-
from rest_framework import permissions

from account.models import BlackList


class BlacklistPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        ip_address = request.META["REMOTE_ADDR"]
        blacklisted = BlackList.objects.filter(ip_address=ip_address).exists()
        return not blacklisted


class BaseModelPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_object_permission(self, request, view, obj):
        has_permission = super().has_permission(request, view)

        if has_permission and view.action == 'retrieve':
            return self._queryset(view).viewable().filter(pk=obj.pk).exists()
        
        if has_permission and view.action == 'list':
            return self._queryset(view).viewable().filter(pk=obj.pk).exists()

        if has_permission and view.action == 'update':
            return self._queryset(view).editable().filter(pk=obj.pk).exists()

        if has_permission and view.action == 'partial_update':
            return self._queryset(view).editable().filter(pk=obj.pk).exists()

        if has_permission and view.action == 'destroy':
            return self._queryset(view).deletable().filter(pk=obj.pk).exists()

        return False