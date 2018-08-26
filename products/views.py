from rest_framework.generics import ListAPIView

from products.models import Product
from products.serializers import ProductSerializer


class ProductList(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, request, *args, **kwargs):
        term = str(request.GET.get('searchTerm', '')).lower()
        return Product.objects.filter(search_terms__term=term)
