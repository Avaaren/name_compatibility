# Generated by Django 3.0.4 on 2020-03-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='percent_in_love',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='percent_in_married',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
