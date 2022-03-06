from django.shortcuts import render


# Create your views here.
from django.template.defaulttags import lorem

from employee_app.employees.models import Employee, Department


def index(request):
    employees = [e for e in Employee.objects.order_by('first_name', 'last_name')]
    context = {
        'number_1': 123,
        'number_2': 321,
        'title': 'EmpYoyeEs List',
        'numbers': [123, 321, 200],
        'description': 'Mario qde mnogo chips i e nadebqlal addadad',
        'employees': employees,
        'department_names': [d.name for d in Department.objects.all()]
    }
    return render(request, 'templates_exercise/template_examples.html', context)
