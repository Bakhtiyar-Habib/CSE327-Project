# Generated by Django 2.0.7 on 2020-05-08 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20200506_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
