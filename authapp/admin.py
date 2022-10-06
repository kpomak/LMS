from django.contrib import admin

from authapp import models as authapp_models


@admin.register(authapp_models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "is_active", "date_joined"]
    list_editable = ["is_active"]
    ordering = ["-date_joined"]
    list_filter = ["is_active", "is_staff"]
