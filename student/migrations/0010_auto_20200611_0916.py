# Generated by Django 3.0.7 on 2020-06-11 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_photo_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='data',
            new_name='date',
        ),
    ]
