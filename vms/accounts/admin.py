from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('username', 'email', 'date_joined', 'last_login', 'admin')
    list_filter = ('admin', 'staff', 'active', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'full_name', 'dept_sec', 'designation', 'contact_no', 'password',
                           'profile_image')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'full_name', 'dept_sec', 'designation', 'contact_no', 'password1', 'password2', 'staff', 'active')}
         ),
    )
    search_fields = ('username', 'email', 'full_name', 'dept_sec', 'designation', 'contact_no')
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
