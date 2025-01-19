from django.shortcuts import get_object_or_404
from products.models import Product


# Source code with variation: https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/4b28dfe82da5e5e24ed830f15ebe4f70deca8886/bag/contexts.py  # noqa
def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    delivery = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
