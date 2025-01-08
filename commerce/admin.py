from django.contrib import admin

from commerce.models import Order, Payment, Coupon, Price

admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Price)