from django.urls import path

from employee_app.employees.views import create_employee, edit_employee

urlpatterns = [
    path('create/', create_employee, name='create'),
    path('edit/<int:pk>', edit_employee, name='edit'),

    # localhost:8000/departments/ -> list of list_departments
    # localhost:8000/departments/1/ -> departments details
    # path('create/', create_department),
    # path('update/', update_department),
    # path('delete/', delete_department),
]
