# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Customize the display fields for the user model in the admin interface
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # Customize the fields that are editable in the admin interface
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Add any additional customizations as needed

admin.site.register(CustomUser, CustomUserAdmin)
