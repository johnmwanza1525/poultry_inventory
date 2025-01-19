from django import template

# Source Code: https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/51702653fda1c506bbe7057376a704f220d82c8b/bag/templatetags/bag_tools.py  # noqa

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
