# Generated by Django 2.0.5 on 2018-08-05 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webdev', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='pyone',
            new_name='phone',
        ),
    ]