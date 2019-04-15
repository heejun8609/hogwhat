from django.contrib import admin
from .models import User, UserInfo
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    list_display = ['username', 'email', 'is_staff']
    list_filter = ['is_staff']
    search_fields = ['username']
    # actions = ['marketing_email']

    # def marketing_email(self, request, queryset):
    #     for user in queryset:
    #         pass
    #     self.message_user(request, 'hello world')

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'species', 'area', 'scale', 'phone', 'created_at']
    search_fields = ['user', 'species', 'area', 'scale']