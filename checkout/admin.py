from django.contrib import admin
from .models import Order, OrderLineItem

# Source code with variation: https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/eee6f2bc60385e58ab27b0732fba3e6a22a2c209/checkout/admin.py  # noqa


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_basket',
                       'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'postcode', 'town_or_city',
              'street_address1', 'street_address2', 'county',
              'delivery_cost', 'order_total', 'grand_total', 'original_basket',
              'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
