# Generated by Django 5.0 on 2023-12-28 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0013_rooms_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rooms',
            old_name='number',
            new_name='floor',
        ),
    ]
