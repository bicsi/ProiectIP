# Generated by Django 2.0.2 on 2018-03-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('path', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('access', models.TextField()),
            ],
        ),
    ]