from django import forms
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from public.mixins import MenuMixin
from public.utils import get_menu_items


class BlogIndexPage(MenuMixin, Page):
    intro = RichTextField(blank=True)
    headline = models.CharField(max_length=127, null=True, blank=True)
    subheadline = models.CharField(max_length=127)
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True, null=True,
        on_delete=models.SET_NULL, related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('headline'),
        FieldPanel('subheadline'),
        ImageChooserPanel('image'),
    ]

    parent_page_types = ['public.HomePage']

    def get_context(self, request):
        context = super().get_context(request)
        context['menuitems'] = get_menu_items()
        context['categories'] = BlogCategory.objects.all().order_by("name")
        blog_posts = BlogPage.objects.all()
        if request.GET.get('category'): 
            blog_posts = blog_posts.filter(category__id=request.GET.get('category'))
        context['blog_posts'] = blog_posts
        return context

class BlogPageTag(TaggedItemBase): 
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name_plural = 'blog categories'



class BlogPage(MenuMixin, Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname='full title')),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', blocks.RawHTMLBlock()),
        ('block_quote', blocks.BlockQuoteBlock()),
    ])
    
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    category = models.ForeignKey(
        'blog.BlogCategory',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True, null=True,
        on_delete=models.SET_NULL, related_name='+')

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('first_published_at'),
            FieldPanel('tags'),
            SnippetChooserPanel('category'), 
        ], heading="Post Details"),
    ]

    parent_page_types = ['blog.BlogIndexPage']

    @property
    def siblings(self):
        return self.get_parent().get_children().order_by('-first_published_at')

    @property
    def sidebar_intro(self):
        if hasattr(self, 'intro'):
            return self.intro
        else:
            return self.get_parent().specific.intro

    def get_context(self, request):
        context = super().get_context(request)
        context['menuitems'] = get_menu_items()
        return context
