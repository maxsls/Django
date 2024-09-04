from django import template

register = template.Library()


@register.filter
def calculate_total(items):
    total = 0
    for item in items:
        total += item.items.price * item.qty

    return total