from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, re_path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^blog/', include(wagtail_urls)),

    path('', TemplateView.as_view(template_name='public/home.html'), name='home'),
    path('contact/', TemplateView.as_view(template_name='public/contact.html'), name='contact'),
]
