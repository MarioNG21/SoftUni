from django import template

register = template.Library()


@register.filter('list')
def make_list_with_key(value):
    return value.split(', ')
