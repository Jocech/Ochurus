# Generated by Django 3.0.2 on 2020-01-23 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20200121_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgcampeon',
            name='url',
            field=models.ImageField(default='default.png', upload_to='imgcampeones'),
        ),
    ]
