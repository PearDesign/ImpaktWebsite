from rest_framework import routers

from companies.views import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='companies')
