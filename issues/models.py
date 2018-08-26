from django.db import models

from products.models import Product
from products.models import Seller


class Issue(models.Model):
    sentiment = models.CharField(
        max_length=32,
        choices=(('positive', 'Positive'), ('negative', 'Negative')),
    )
    headline = models.CharField(max_length=128)
    description = models.TextField()
    reference = models.URLField(blank=True, null=True)

    class Meta:
        abstract = True


class ProductIssue(Issue):
    '''Individual concerning (or positive) item pertaining to a product'''
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_issues')


class SellerIssue(Issue):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='seller_issues')
