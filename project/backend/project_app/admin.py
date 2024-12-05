from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Display these fields in the list view of the Django admin
    list_display = ('username', 'email', 'user_type', 'contact_number', 'is_approved', 'is_email_verified', 'is_active', 'created_at')
    # Enable filtering by these fields
    list_filter = ('user_type', 'is_approved', 'is_email_verified', 'is_active')
    # Specify the fields to search
    search_fields = ('username', 'email', 'contact_number')
    # Add 'contact_number', 'user_type', and 'is_approved' to the user creation form
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'contact_number', 'is_approved', 'is_email_verified')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type', 'contact_number', 'is_approved', 'is_email_verified')}),
    )

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)
