# Generated by Django 2.2.3 on 2020-01-25 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_auto_20200125_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campeon',
            name='msj',
        ),
        migrations.RemoveField(
            model_name='campeon',
            name='votos',
        ),
    ]
