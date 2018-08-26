from django.contrib import admin

from issues.admin import ProductIssueInline
from issues.admin import SellerIssueInline
from products.models import Product
from products.models import SearchTerm
from products.models import Seller


@admin.register(SearchTerm)
class SearchTermAdmin(admin.ModelAdmin):
    pass


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    inlines = [
        SellerIssueInline,
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductIssueInline,
    ]
