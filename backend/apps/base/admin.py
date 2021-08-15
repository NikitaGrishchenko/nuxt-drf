from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group as BaseGroup

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("email", "first_name", "last_name", "date_of_birth")
    ordering = ("pk",)
    # list_filter = ("email",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "photo",
                    "date_of_birth",
                )
            },
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )


# admin.site.unregister(BaseGroup)

# admin.site.register(ProxyGroup, GroupAdmin)
