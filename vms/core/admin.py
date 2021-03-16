from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import NewUser


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'username', 'email', 'contact_no', 'admin')
    list_filter = ('admin', 'staff', 'active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'full_name', 'dept_sec', 'designation', 'contact_no', 'password',)}),
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


admin.site.register(NewUser, UserAdmin)
