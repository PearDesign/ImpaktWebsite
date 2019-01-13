from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    subheadline = models.CharField(max_length=127)
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True, null=True,
        on_delete=models.SET_NULL, related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('subheadline'),
        ImageChooserPanel('image'),
    ]


class BlogPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname='full title')),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', blocks.RawHTMLBlock()),
        ('block_quote', blocks.BlockQuoteBlock()),
    ])

    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True, null=True,
        on_delete=models.SET_NULL, related_name='+')

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('first_published_at'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]

    @property
    def siblings(self):
        return self.get_parent().get_children().order_by('-first_published_at')

    @property
    def sidebar_intro(self):
        if hasattr(self, 'intro'):
            return self.intro
        else:
            return self.get_parent().specific.intro