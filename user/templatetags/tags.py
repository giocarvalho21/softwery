from django import template

register = template.Library()

@register.simple_tag
def dateToday():
    return 'funcionando'