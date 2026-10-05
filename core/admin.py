from django.contrib import admin
from .models import Employee,Project

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=[
        'employee_id',
        'name',
        'email',
        'phone',
        'department',
        'designation',
        'date_of_joining',
        'salary',
        'is_active',
    ]
    search_fields=[
        'name',
        'employee_id',
    ]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display= [
        'project_name',
        'client_name',
        'project_manager',
        'start_date',
        'end_date',
        'status',
    ]
    list_filter=['status']

    search_fields=[
        'project_name',
        'client_name',
    ]
