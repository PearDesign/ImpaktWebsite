from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from products.models import Product
from products.serializers import ProductSerializer


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        term = self.kwargs.get('search_term', '').lower()
        return Product.objects.filter(search_terms__term=term)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        query_filter = {
            'seller__asin': self.kwargs.get('seller__ASIN', '').lower(),
            'slug': self.kwargs.get('product_slug', '').lower(),
        }
        obj = get_object_or_404(queryset, **query_filter)
        self.check_object_permissions(self.request, obj)
        return obj
