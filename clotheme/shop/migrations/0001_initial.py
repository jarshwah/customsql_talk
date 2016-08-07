# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Kids', 'Kids'), ('Men', 'Men'), ('Women', 'Women')], max_length=10)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateTimeField()),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('state', models.CharField(choices=[('VIC', 'VIC'), ('NSW', 'NSW'), ('QLD', 'QLD'), ('TAS', 'TAS'), ('SA', 'SA'), ('WA', 'WA')], max_length=3)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
    ]
