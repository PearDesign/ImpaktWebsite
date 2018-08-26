from rest_framework import serializers
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from products.models import Product
from products.models import SearchTerm


class SearchTermSerializer(TaggitSerializer, serializers.ModelSerializer):

    class Meta:
        exclude = ('id', )
        model = SearchTerm


class ProductSerializer(serializers.ModelSerializer):
    search_terms = SearchTermSerializer(read_only=True, many=True)
    tags = TagListSerializerField()

    class Meta:
        exclude = ('id', )
        model = Product
