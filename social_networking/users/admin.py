from django.contrib import admin
from base.admin import BaseModelAdmin
from users.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(BaseModelAdmin):
    search_fields = ('uuid', 'user__email', 'mobile', 'name', 'is_verified')
    list_display = (
        'uuid', 'user', 'mobile', 'name', 'is_verified')
