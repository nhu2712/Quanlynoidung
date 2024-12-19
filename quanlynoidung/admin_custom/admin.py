from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Employee


admin.site.unregister(Group)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'permission', 'position', 'department')
