# Generated by Django 5.0 on 2024-01-03 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0027_alter_apartment_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='floor',
            old_name='title',
            new_name='number',
        ),
    ]
