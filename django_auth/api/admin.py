from django.contrib import admin
from api.models import User


@admin.register(User)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'role',
    )
    search_fields = ('username', 'email')
    empty_value_display = '-пусто-'