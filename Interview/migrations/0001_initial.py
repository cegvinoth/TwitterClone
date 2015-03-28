# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('following_id', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notify_type', models.CharField(max_length=50)),
                ('notify_createdby', models.IntegerField()),
                ('notify_post_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_data', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('firstname', models.CharField(max_length=24)),
                ('lastname', models.CharField(max_length=24)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('password', models.CharField(max_length=24)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(to='Interview.users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='follow',
            name='user_id',
            field=models.ForeignKey(to='Interview.users'),
            preserve_default=True,
        ),
    ]
