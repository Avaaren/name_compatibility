# Generated by Django 3.0.4 on 2020-03-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0003_auto_20200323_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='slug',
            field=models.SlugField(default='s'),
        ),
    ]
