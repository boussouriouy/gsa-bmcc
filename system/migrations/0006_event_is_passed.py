# Generated by Django 3.0.7 on 2020-06-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20200612_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_passed',
            field=models.BooleanField(default=False),
        ),
    ]
