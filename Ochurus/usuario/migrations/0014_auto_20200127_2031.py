# Generated by Django 2.2.3 on 2020-01-27 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0013_item_camp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='camp',
        ),
        migrations.CreateModel(
            name='ItemCampeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Campeon')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Item')),
            ],
        ),
    ]