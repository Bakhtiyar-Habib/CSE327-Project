# Generated by Django 2.0.7 on 2020-05-10 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_auto_20200510_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='link',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
