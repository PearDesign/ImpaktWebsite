from django.db import models
from taggit.managers import TaggableManager


class Seller(models.Model):
    '''A company selling products on Amazon'''
    ASIN = models.CharField(max_length=128, db_index=True, unique=True)
    tags = TaggableManager()


class Product(models.Model):
    '''Representation of a project on Amazon'''
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    slug = models.CharField(max_length=512, db_index=True, unique=True)
    tags = TaggableManager()
