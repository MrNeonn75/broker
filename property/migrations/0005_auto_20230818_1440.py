# Generated by Django 3.2.19 on 2023-08-18 10:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20230818_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='property.areamodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 18, 14, 40, 48, 504230), verbose_name='Date'),
        ),
    ]