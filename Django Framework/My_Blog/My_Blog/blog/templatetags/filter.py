from django import template

register = template.Library()


@register.filter('capitalize')
def capitalize(value):
    return value[0].upper() + value[1:]
