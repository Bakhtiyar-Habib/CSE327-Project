# Generated by Django 2.0.7 on 2020-05-07 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formalmen',
            name='url',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='formalwomen',
            name='url',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
