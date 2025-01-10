from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'is_staff_user', 'is_end_user', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_staff_user', 'is_end_user')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_staff_user', 'is_end_user')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)