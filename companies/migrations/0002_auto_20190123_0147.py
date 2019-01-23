# Generated by Django 2.1.5 on 2019-01-23 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='negative_image',
            field=models.ImageField(blank=True, help_text='Icon to display when a company scores negatively on this metric', null=True, upload_to='', verbose_name='Negative Image'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='neutral_image',
            field=models.ImageField(blank=True, help_text='Icon to display when a company scores neutrally on this metric', null=True, upload_to='', verbose_name='Neutral Image'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='positive_image',
            field=models.ImageField(blank=True, help_text='Icon to display when a company scores positively on this metric', null=True, upload_to='', verbose_name='Positive Image'),
        ),
    ]
