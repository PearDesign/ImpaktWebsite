# Generated by Django 2.1 on 2018-08-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]