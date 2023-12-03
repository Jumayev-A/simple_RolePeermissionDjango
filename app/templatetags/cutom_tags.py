from django import template

register = template.Library()


@register.filter()
def split(value, arg):
    """Removes all values of arg from the given string"""
    return str(value).split(f"{arg}")