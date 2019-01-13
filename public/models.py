from wagtail.core.models import Page


class HomePage(Page):
    parent_page_types = ['wagtailcore.Page']


class ContactPage(Page):
    parent_page_types = ['wagtailcore.Page']
