# Generated by Django 5.1.6 on 2025-02-27 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='title',
        ),
    ]
