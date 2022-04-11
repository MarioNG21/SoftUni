from django.contrib import admin

from My_final_social_media_shop.auth_acc.models import AppUser, Profile


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'is_active', 'is_staff', 'is_superuser')
    readonly_fields = ('password', 'last_login')
    list_filter = ('date_joined', 'email')
    list_display_links = ('email', 'date_joined', 'is_superuser')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'gender', 'phone')
    empty_value_display = '--empty--'
    list_filter = ('age', 'first_name')
    list_display_links = ('first_name', 'last_name')
