# Generated by Django 2.0.7 on 2020-05-29 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0011_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
