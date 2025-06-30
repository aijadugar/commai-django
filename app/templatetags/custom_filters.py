from django import template

register = template.Library()

@register.filter
def get_key(dictionary, key):
    """Retrieve a dictionary value by key in Django templates."""
    return dictionary.get(key, [])
