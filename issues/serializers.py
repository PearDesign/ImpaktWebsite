from rest_framework import serializers

from issues.models import ProductIssue
from issues.models import SellerIssue


class ProductIssueSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id', )
        model = ProductIssue


class SellerIssueSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id', )
        model = SellerIssue
