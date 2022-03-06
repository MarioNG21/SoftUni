from django.contrib import admin

# Register your models here.
from employee_app.mario.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
