from django.contrib import admin
from application.order.models import Order, Archive

admin.site.register(Order)
admin.site.register(Archive)