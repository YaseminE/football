# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 07:10
from __future__ import unicode_literals

from django.db import migrations


def create_age_groups(apps, schema_editor):
    AgeGroup = apps.get_model('players', 'AgeGroup')
    AgeGroup.objects.get_or_create(name='U11', description='Yr6 on or after 1st September 2017')
    AgeGroup.objects.get_or_create(name='U12', description='Yr7 on or after 1st September 2017')
    AgeGroup.objects.get_or_create(name='U13', description='Yr8 on or after 1st September 2017')
    AgeGroup.objects.get_or_create(name='U14', description='Yr9 on or after 1st September 2017')
    AgeGroup.objects.get_or_create(name='U15', description='Yr10 on or after 1st September 2017')


def create_field_positions(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    FieldPosition = apps.get_model('players', 'FieldPosition')
    FieldPosition.objects.get_or_create(name='Left Back')
    FieldPosition.objects.get_or_create(name='Centre Back (Left)‎')
    FieldPosition.objects.get_or_create(name='Centre Back (Right)‎')
    FieldPosition.objects.get_or_create(name='Right Back‎')
    FieldPosition.objects.get_or_create(name='Midfield‎')
    FieldPosition.objects.get_or_create(name='Attacking Mid‎')
    FieldPosition.objects.get_or_create(name='Left Wing‎')
    FieldPosition.objects.get_or_create(name='Right Wing‎')
    FieldPosition.objects.get_or_create(name='Forward (Left/Centre/Right)‎')
    FieldPosition.objects.get_or_create(name='Striker‎‎')


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_age_groups),
        migrations.RunPython(create_field_positions),
    ]
