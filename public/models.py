from wagtail.core.models import Page

from public.mixins import MenuMixin
from public.utils import get_menu_items


class HomePage(MenuMixin, Page):
    parent_page_types = ['wagtailcore.Page']

    def get_context(self, request):
        context = super().get_context(request)
        context['menuitems'] = get_menu_items()
        return context


class ContactPage(MenuMixin, Page):
    parent_page_types = ['public.HomePage']

    def get_context(self, request):
        context = super().get_context(request)
        context['menuitems'] = get_menu_items()
        return context
