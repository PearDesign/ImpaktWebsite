# Generated by Django 2.1.5 on 2019-01-30 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='headline',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
    ]