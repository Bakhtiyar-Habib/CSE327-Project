# Generated by Django 2.0.7 on 2020-05-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, default='default.jpg', upload_to='')),
                ('subcategories', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]
