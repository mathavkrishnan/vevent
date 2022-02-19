from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import user, events

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff','is_club', 'is_student']
    list_filter = ['is_student', 'is_club']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields':('is_student', 'is_club')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_student', 'is_club')
        }),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(user, CustomUserAdmin)
admin.site.register(events)