# Generated by Django 3.1.5 on 2021-01-09 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshorten', '0002_urlshortener_click'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlshortener',
            old_name='click',
            new_name='clicks_count',
        ),
    ]
