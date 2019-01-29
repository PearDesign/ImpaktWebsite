from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
        FieldPanel, FieldRowPanel,
        InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel

from public.mixins import MenuMixin
from public.utils import get_menu_items


class HomePage(MenuMixin, Page):
    parent_page_types = ['wagtailcore.Page']

    def get_context(self, request):
        context = super().get_context(request)
        context['menuitems'] = get_menu_items()
        return context


class FormField(AbstractFormField):
    page = ParentalKey('ContactFormPage', on_delete=models.CASCADE, related_name='form_fields')


class ContactFormPage(MenuMixin, AbstractEmailForm):
    intro = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True, null=True,
        on_delete=models.SET_NULL, related_name='+')
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('image'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['menuitems'] = get_menu_items()
        return context
