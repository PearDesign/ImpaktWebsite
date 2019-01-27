import os
import pandas as pd

from django.conf import settings
from django.core.management.base import BaseCommand

from companies.models import Assessment
from companies.models import Incident
from companies.models import Company
from companies.models import Metric


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        filepath = os.path.join(
            settings.BASE_DIR,
            'companies/fixtures/report.csv')
        df = pd.read_csv(filepath)

        # Create metrics from supplied data
        for header in df.columns.values:
            metric_name = get_metric_name_from_header(header)
            if not metric_name:
                continue
            metric, created = Metric.objects.get_or_create(text=metric_name)

            if not metric:
                continue

            for index, row in df.iterrows():
                company, created = Company.objects.get_or_create(
                    sustainalytics_id=row.CompanyId,
                    defaults={
                        'name': row.CompanyName,
                    })

                try:
                    value = row[header]
                except KeyError:
                    continue
                if not value or str(value) == 'nan':
                    continue
                if type(value) == int:
                    # Assessment

                    justification = row.get(header + ' justification', '')
                    Assessment.objects.get_or_create(
                        company=company,
                        metric=metric,
                        data_source='sustainalytics',
                        defaults={
                            'justification': justification,
                            'sentiment': 'negative' if value == 1 else 'strongly_negative',
                        })
                else:
                    # Incident
                    Incident.objects.get_or_create(
                        company=company,
                        metric=metric,
                        defaults={
                            'text': value,
                        })


def get_metric_name_from_header(header):
    '''String formats metric names to be more readable'''
    if header in ['CompanyName', 'CompanyId', 'CompanyName.1']:
        return None
    elif header.count('.') > 1:
        header = header.split(" ", 1)[1]
    elif ' - ' in header:
        header = header.split(' - ')[0].strip()
    header = header\
        .replace('-Assessment', '')\
        .replace('-Summary', '')\
        .replace('-Answer category', '')\
        .replace('-Answer category justification', '')
    if header.endswith(' justification'):
        header = header.split(' justification')[0]
    return header
