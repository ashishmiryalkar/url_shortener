# Generated by Django 3.1.5 on 2021-01-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLShortener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=10)),
                ('actual_url', models.CharField(max_length=200)),
            ],
        ),
    ]
