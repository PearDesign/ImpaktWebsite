from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from companies.models import Company, Metric
from companies.serializers import CompanySerializer
from companies.serializers import MetricSerializer


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def retrieve(self, request, pk=None):
        try:
            company = Company.objects.get(ASIN=pk)
        except Company.DoesNotExist:
            company = get_object_or_404(self.queryset, slug=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)


class MetricViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MetricSerializer
    queryset = Metric.objects.all()
