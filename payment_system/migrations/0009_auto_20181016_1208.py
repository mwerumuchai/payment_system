# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-16 09:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0008_auto_20181016_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactrecipient',
            old_name='fullname',
            new_name='full_name',
        ),
    ]
