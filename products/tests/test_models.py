from django.test import TestCase

from products.factories import ProductFactory
from products.factories import SellerFactory
from products.models import Product
from products.models import Seller


class ModelTestCaseMixin:

    def test_factory_create(self):
        obj = self.factory()
        self.assertIsInstance(obj, self.model_class)

    def test_factory_read(self):
        obj = self.factory()
        self.assertTrue(getattr(obj, self.example_attr))

    def test_factory_update(self):
        obj = self.factory(**{self.example_attr: 'foo'})
        setattr(obj, self.example_attr, 'bar')
        obj.save()
        obj.refresh_from_db()
        self.assertEqual(getattr(obj, self.example_attr), 'bar')

    def test_factory_delete(self):
        obj = self.factory()
        self.assertEqual(self.model_class.objects.all().count(), 1)
        obj.delete()
        self.assertEqual(self.model_class.objects.all().count(), 0)


class SellerTestCase(ModelTestCaseMixin, TestCase):
    example_attr = 'ASIN'
    factory = SellerFactory
    model_class = Seller


class ProductTestCase(ModelTestCaseMixin, TestCase):
    example_attr = 'slug'
    factory = ProductFactory
    model_class = Product
