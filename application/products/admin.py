from django.contrib import admin
from application.products.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)