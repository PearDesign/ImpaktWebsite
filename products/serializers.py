from rest_framework import serializers
from issues.serializers import ProductIssueSerializer
from products.models import Product
from products.models import SearchTerm
from products.models import Seller


class SearchTermSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id', )
        model = SearchTerm


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id', )
        model = Seller


class ProductSerializer(serializers.ModelSerializer):
    product_issues = ProductIssueSerializer(read_only=True, many=True)
    search_terms = SearchTermSerializer(read_only=True, many=True)
    seller = SellerSerializer(read_only=True)

    class Meta:
        exclude = ('id', )
        model = Product
