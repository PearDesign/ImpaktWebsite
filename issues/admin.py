from django.contrib import admin

from issues.models import ProductIssue
from issues.models import SellerIssue


class ProductIssueInline(admin.TabularInline):
    extra = 1
    model = ProductIssue


class SellerIssueInline(admin.TabularInline):
    extra = 1
    model = SellerIssue
