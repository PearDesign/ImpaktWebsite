from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=511, db_index=True)
    link = models.CharField(max_length=1023, null=True, blank=True)
    text = models.TextField()
