# Generated by Django 3.2.9 on 2021-11-24 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barba', '0008_auto_20211121_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
