# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-02-13 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0008_user_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_post',
            name='images',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
    ]