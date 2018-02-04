# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-04 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180204_0412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=15)),
                ('size', models.CharField(max_length=2)),
                ('cc_amount', models.CharField(max_length=30)),
                ('asset_size', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'financial',
            },
        ),
        migrations.CreateModel(
            name='MicroBusiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.DecimalField(decimal_places=3, max_digits=8)),
                ('amount', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'microbusiness',
            },
        ),
        migrations.CreateModel(
            name='SmallBusiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.DecimalField(decimal_places=3, max_digits=8)),
                ('ratio_ta', models.DecimalField(decimal_places=3, max_digits=8)),
                ('ratio_tbl', models.DecimalField(decimal_places=3, max_digits=8)),
                ('amount', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'smallbusiness',
            },
        ),
        migrations.DeleteModel(
            name='Map',
        ),
        migrations.RemoveField(
            model_name='legislation',
            name='maps',
        ),
        migrations.AddField(
            model_name='legislation',
            name='summary',
            field=models.TextField(default='none', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='smallbusiness',
            unique_together=set([('rank', 'amount', 'number', 'ratio_ta', 'ratio_tbl')]),
        ),
        migrations.AlterUniqueTogether(
            name='microbusiness',
            unique_together=set([('rank', 'amount', 'number')]),
        ),
        migrations.AddField(
            model_name='financial',
            name='micro_business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.MicroBusiness'),
        ),
        migrations.AddField(
            model_name='financial',
            name='small_business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.SmallBusiness'),
        ),
    ]