from django.contrib import admin

from products.models import Product
from products.models import Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
