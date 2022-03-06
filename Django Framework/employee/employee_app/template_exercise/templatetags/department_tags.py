from django import template

from employee_app.employees.models import Department

register = template.Library()


@register.inclusion_tag('tag/departments_list.html')
def departments_list():
    departments = Department.objects\
        .prefetch_related('employee_set') \
        .all()

    #context

    return {
        'departments': departments
    }