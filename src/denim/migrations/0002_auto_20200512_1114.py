# Generated by Django 2.0.7 on 2020-05-12 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='denimmen',
            name='price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='denimwomen',
            name='price',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
