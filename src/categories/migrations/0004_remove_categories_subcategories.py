# Generated by Django 2.0.7 on 2020-05-17 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_categories_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='subcategories',
        ),
    ]