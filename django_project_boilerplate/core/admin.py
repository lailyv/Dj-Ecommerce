from django.contrib import admin

from .models import Address, Item, Order, OrderItem, Payment, Coupon, Refund
# Register your models here.


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_grandted=True)


make_refund_accepted.short_description = 'Update Order to Refund Grandted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'billing_address',
                    'shipping_address',
                    'payment',
                    'coupon']
    list_display_links = ['user',
                          'billing_address',
                          'shipping_address',
                          'payment',
                          'coupon']
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    action = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default',
    ]
    list_filter = ['default', 'address_type', 'country']
    list_search = ['user', 'street_address', 'apartment_address', 'zip']


admin.site.register(Coupon)
admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Refund)
admin.site.register(Payment)
admin.site.register(Address, AddressAdmin)
