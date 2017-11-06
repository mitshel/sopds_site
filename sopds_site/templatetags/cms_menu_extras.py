from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def splitmenu(value,n):
    v = value.split('|')
    return v[n] if n<=len(v)-1 else ''