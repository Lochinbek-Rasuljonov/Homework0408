# Generated by Django 5.1 on 2025-01-31 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Category_FastFood',
        ),
        migrations.RenameModel(
            old_name='Food',
            new_name='FastFood',
        ),
    ]
