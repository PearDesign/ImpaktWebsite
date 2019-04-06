# Generated by Django 2.2 on 2019-04-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20190127_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='data_source',
            field=models.CharField(choices=[('impakt', 'Directly-supplied by Impakt researchers'), ('sustainalytics', 'Sustainalytics'), ('nyu', 'NYU Researchers')], db_index=True, help_text='Where the information for this assessment came from', max_length=127, verbose_name='Data Source'),
        ),
    ]
