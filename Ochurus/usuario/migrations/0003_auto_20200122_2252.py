# Generated by Django 2.2.5 on 2020-01-23 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20200121_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='imgcampeon',
            name='url',
            field=models.ImageField(default='default.png', upload_to='imgcampeones'),
        ),
    ]
