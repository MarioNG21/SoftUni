from django.contrib import admin

# Register your models here.
from employee_app.employees.models import Employee, Department, Project


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'company', 'job_title', 'department_id')


@admin.register(Department)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'dead_line')
