import os
import pandas as pd

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        filepath = os.path.join(
            settings.BASE_DIR,
            'companies/fixtures/report.csv')
        df = pd.read_csv(filepath)
        header_names = []
        for header in list(df.columns.values):
            header_names.append(header.split("-")[0].strip())
        metric_names = list(set(header_names))
        print(metric_names)
