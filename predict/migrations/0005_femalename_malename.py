# Generated by Django 3.0.4 on 2020-03-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0004_relationship_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='FemaleName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='MaleName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
