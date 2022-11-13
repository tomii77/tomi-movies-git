from django import template
import math

register = template.Library()

@register.filter
def round_up(value):
    return int(math.ceil(value / 1000.0) * 1000.0)