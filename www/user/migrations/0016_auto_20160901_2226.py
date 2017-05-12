# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20160901_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyRecommendMerg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('job_id', models.IntegerField()),
                ('recommend_num', models.IntegerField()),
            ],
            options={
                'db_table': 'my_recommend_merg',
            },
        ),
        migrations.AlterField(
            model_name='myrecommend',
            name='user_id',
            field=models.IntegerField(),
        ),
        migrations.AlterIndexTogether(
            name='myrecommend',
            index_together=set([('user_id', 'job_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='myrecommendmerg',
            unique_together=set([('user_id', 'job_id')]),
        ),
    ]