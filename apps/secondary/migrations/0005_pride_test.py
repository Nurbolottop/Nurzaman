# Generated by Django 5.0 on 2023-12-22 00:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0004_pride'),
    ]

    operations = [
        migrations.AddField(
            model_name='pride',
            name='test',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст'),
        ),
    ]