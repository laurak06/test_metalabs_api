from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, LoginLog
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # какие поля отображать в списке
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "date_joined", "last_login")

    # фильтрация сбоку
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")

    # поиск
    search_fields = ("username", "email", "first_name", "last_name")

    # порядок сортировки по умолчанию
    ordering = ("-date_joined",)


@admin.register(LoginLog)
class LoginLogAdmin(admin.ModelAdmin):
    # отображаются в списке
    list_display = ('user', 'timestamp', 'ip_address', 'user_agent')

    # по которым можно фильтровать
    list_filter = ('user', 'timestamp')

    # по которым можно искать
    search_fields = ('user__username', 'ip_address', 'user_agent')

    # сортировка по умолчанию
    ordering = ('-timestamp',)
