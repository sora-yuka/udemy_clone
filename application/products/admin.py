from django.contrib import admin
from application.products.models import (
    Product, ProductFile, ProductItem, Category
)

admin.site.register(Product)
admin.site.register(ProductFile)
admin.site.register(ProductItem)
admin.site.register(Category)