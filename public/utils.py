from wagtail.core.models import Page


def get_menu_items():
    return Page.objects.filter(show_in_menus=True).order_by('id')
