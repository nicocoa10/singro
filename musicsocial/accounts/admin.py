from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('profile_pic','first_name','favorite_genre', 'about','music_link')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'first_name','profile_pic','favorite_genre', 'about','music_link', 'is_staff')
    search_fields = ('username', 'first_name', 'favorite_genre')
    ordering = ('username',)



admin.site.register(get_user_model(),CustomUserAdmin)