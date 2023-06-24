from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Courier

        
class UserAdmin(BaseUserAdmin):
    """
        this class is UserAdmin class and set fields of admin page of
        User model.
    """
    model = User
    list_display = ('phone', 'is_superuser', 'is_active')
    list_filter = ('phone', 'is_superuser', 'is_active')
    search_fields = ('phone', )
    ordering = ('created_date', )
    readonly_fields = ['created_date', 'updated_date', 'last_login']
    fieldsets = (
        ('Authentication', {
            "fields": (
                'phone',
                'password',
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff',
                'is_active',
                'is_superuser',
            ),
        }),
        ('Group Permissions', {
            "fields": (
                'groups',
                'user_permissions',
            ),
        }),
        ('Important Dates', {
            "fields": (
                'last_login',
                'created_date',
                'updated_date',
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone", "password1", "password2", "is_staff", "is_active", "is_superuser")
        }),
    )
    
class CourierAdmin(BaseUserAdmin):
    """
        this class is UserAdmin class and set fields of admin page of
        User model.
    """
    model = User
    list_display = ('phone', 'is_available', 'latitude', 'longitude', 'is_available')
    list_filter = ('phone', 'is_available', 'latitude', 'longitude', 'is_available')
    search_fields = ('phone', )
    ordering = ('created_date', )
    readonly_fields = ['created_date', 'updated_date', 'last_login']
    fieldsets = (
        ('Authentication', {
            "fields": (
                'phone',
                'password',
            ),
        }),
        ('Status', {
            "fields": (
                'is_available',
            ),
        }),
        ('Important Dates', {
            "fields": (
                'last_login',
                'created_date',
                'updated_date',
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone", "password1", "password2", "latitude", "longitude",)
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Courier, CourierAdmin)