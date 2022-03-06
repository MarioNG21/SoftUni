from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from employee_app.employees.models import Employee


def validate_positive(value):
    if value < 0:
        raise ValidationError('Value must be positive')
    return


class EmployeeForm(forms.ModelForm):
    def clean(self):
        
        return self.cleaned_data

    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }
            )
        }


class EmployeeOrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'first_name'),
            ('last_name', 'last_name')
        )
    )


class EditEmployeeForm(EmployeeForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(
                attrs={
                    'disabled': 'disabled'
                }
            )
        }


# class EmployeeForm(forms.Form):
#     GOOGLE = 'Google'
#     SOFT_UNI = 'Soft Uni'
#     first_name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )
#
#     last_name = forms.CharField(
#         max_length=40,
#         widget=forms.TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )
#
#     age = forms.IntegerField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         validators=(
#             validate_positive,
#         )
#     )
#
#     job_title = forms.ChoiceField(
#         choices=(
#             (1, 'Software Developer'),
#             (2, 'QA Engineer'),
#             (3, 'DevOps Specialist')
#         ),
#
#     )
#
#     egn = forms.CharField(
#         max_length=19
#     )
#     company = forms.ChoiceField(
#         choices=(
#             (GOOGLE, GOOGLE),
#             (SOFT_UNI, SOFT_UNI)
#         )
#     )


def home(request):
    return render(request, 'index.html')


def create_employee(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            # Version 1 -> най старият начин
            # first_name = employee_form.cleaned_data.get('first_name')
            # last_name = employee_form.cleaned_data.get('last')
            # age = 20
            # job_title = employee_form.cleaned_data.get('job_title')
            # egn = employee_form.cleaned_data.get('egn')
            # company = employee_form.cleaned_data.get('company')
            # department_id = 1,
            # emp = Employee(first_name=first_name, last_name=last_name, job_title=job_title, egn=egn, age=age, company=company, department_id=department_id)
            # emp.save()
            # Version 2.0 по лесен начин
            # emp = Employee(**employee_form.cleaned_data,
            #                department_id=1)
            # emp.save()
            # Version 3.0 -> ModelForm way to save
            employee_form.save()

            return redirect('index')

    else:
        employee_form = EmployeeForm()
    employee_order_form = EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name')

    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.all().order_by(order_by),
        'employee_order_form': employee_order_form
    }
    return render(request, 'create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == "GET":
        employee_form = EditEmployeeForm(instance=employee)

    else:
        employee_form = EditEmployeeForm(request.POST, instance=employee)
        if employee_form.is_valid():
            employee_form.save()

    context = {
        'employee_form': employee_form,
        'employee': employee,

    }
    return render(request, 'edit.html', context)

# Old worst case
# def create_employee(request):
#     if request.method == 'GET':
#         context = {
#             'employee_form': EmployeeForm()
#         }
#         return render(request, 'create.html', context)
#         # Show data
#     else:
#
#         employee_form = EmployeeForm(request.POST)
#         if employee_form.is_valid():
#             return redirect('index')
#         context = {
#             'employee_form': employee_form
#         }
#         return render(request, 'create.html', context)
#
#
#


# def not_found(request):
#     return HttpResponseNotFound()
#
#
# def go_to_home(request):
#     return redirect('department_details', id=random.randint(0, 1024))
#
#
# def department_details(request, id):
#     return HttpResponse(f'This is department {id}')
#
#
# def list_departments(request):
#     context = {
#         'departments': Department.objects.prefetch_related('employee_set'),
#         'employees': Employee.objects.all(),
#     }
#     return render(request, 'list_of_departments.html', context)
#
#
# def list_employees(request):
#
#     context = {
#         'employees': Employee.objects.all(),
#         'projects': Project.objects.all(),
#     }
#
#     return render(request, 'employees.html', context)
