# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-04 15:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20171204_0010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='CollegeName',
            new_name='college',
        ),
    ]