import factory


class SellerFactory(factory.django.DjangoModelFactory):
    ASIN = factory.Faker('word')

    class Meta:
        model = 'products.Seller'


class ProductFactory(factory.django.DjangoModelFactory):
    seller = factory.SubFactory(SellerFactory)
    slug = factory.Faker('slug')

    class Meta:
        model = 'products.Product'
