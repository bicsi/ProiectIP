# Generated by Django 2.0.5 on 2018-05-10 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20180510_1318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created']},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['created']},
        ),
    ]