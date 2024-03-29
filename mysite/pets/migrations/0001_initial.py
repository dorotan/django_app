# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=200)),
                ('when_born', models.DateTimeField(verbose_name='when was pet born')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.Pet'),
        ),
    ]
