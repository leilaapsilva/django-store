# Generated by Django 3.0.8 on 2020-07-15 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='creation_date',
            field=models.DateTimeField(null=True, verbose_name='creation date'),
        ),
    ]