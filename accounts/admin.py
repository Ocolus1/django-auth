from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Company, Category as Cat, Stage


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'name', 'is_staff')
    search_fields = ('name', 'email')
    ordering = ('email',)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(CustomUser, UserAdmin)

# @admin.register(CustomUser)
# class CustomUserAdmin(BaseUserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = [
#         "email",
#         "username",
#     ]

admin.site.register(Company)
admin.site.register(Cat)
admin.site.register(Stage)