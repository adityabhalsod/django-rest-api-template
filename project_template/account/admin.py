# accounts.admin.py
from django.contrib import admin
from django.contrib.auth.models import Group, Permission

from base.admin import BaseAdmin

from .models import BlackList, User
from account.form import GroupAdminForm


# Unregister the original Group admin.
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseAdmin):
    exclude = (
        "is_staff",
        "is_active",
        "is_superuser",
        "groups",
        "user_permissions",
    )


@admin.register(Permission)
class PermissionAdmin(BaseAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, reques, obj=None):
        return False
    
    def has_change_permission(self, reques, obj=None):
        return False


@admin.register(BlackList)
class BlacklistAdmin(BaseAdmin):
    pass


# Create a new Group admin.
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

