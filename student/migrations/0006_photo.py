# Generated by Django 3.0.7 on 2020-06-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20200611_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_1', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]
