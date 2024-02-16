# Generated by Django 5.0 on 2023-12-22 00:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_pride_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pride',
            old_name='test',
            new_name='first',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='first_descriptions',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='first_subtitle',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='first_title',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='five_descriptions',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='five_subtitle',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='five_title',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='four_descriptions',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='four_subtitle',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='four_title',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='second_descriptions',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='second_subtitle',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='second_title',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='six_descriptions',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='six_subtitle',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='six_title',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='third_descriptions',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='third_subtitle',
        ),
        migrations.RemoveField(
            model_name='pride',
            name='third_title',
        ),
        migrations.AddField(
            model_name='pride',
            name='five',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст'),
        ),
        migrations.AddField(
            model_name='pride',
            name='four',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст'),
        ),
        migrations.AddField(
            model_name='pride',
            name='second',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст'),
        ),
        migrations.AddField(
            model_name='pride',
            name='six',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст'),
        ),
        migrations.AddField(
            model_name='pride',
            name='third',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст'),
        ),
    ]
