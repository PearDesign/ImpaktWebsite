from django.db import models
from taggit.managers import TaggableManager


class SearchTerm(models.Model):
    '''Term that users can search for on Amazon

    This model is linked to products via a ManyToMany relationship. When a user visits a search
    page, they'll information about any products joined to their particular search term.
    '''
    term = models.CharField(max_length=256, unique=True)

    def save(self, *args, **kwargs):
        self.term = self.term.lower()
        super(SearchTerm, self).save(*args, **kwargs)


class Seller(models.Model):
    '''A company selling products on Amazon'''
    ASIN = models.CharField(max_length=128, db_index=True, unique=True)
    name = models.CharField(max_length=256)
    tags = TaggableManager()

    def __str__(self):
        return "{0}, ASIN: {1}".format(self.name, self.ASIN)


class Product(models.Model):
    '''Representation of a project on Amazon'''
    name = models.CharField(max_length=256)
    search_terms = models.ManyToManyField(SearchTerm)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    slug = models.CharField(max_length=512, db_index=True, unique=True)
    tags = TaggableManager()

    def __str__(self):
        return "{0}, sold by {1}".format(self.short_name, self.seller.name)

    @property
    def short_name(self, chars=50):
        if len(self.name) > chars:
            return self.name[:chars] + "..."
        else:
            return self.name
