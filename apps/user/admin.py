from django.contrib import admin

from unfold.admin import ModelAdmin

from apps.user.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('email', 'provider', 'nickname', 'is_staff')
    list_filter = ('provider', )
    search_fields = ('email', 'nickname')
