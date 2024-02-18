# Generated by Django 5.0 on 2023-12-26 21:27

import ckeditor.fields
import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0015_alter_choise_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvantagesTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст')),
            ],
            options={
                'verbose_name': 'Преимущества номер один',
                'verbose_name_plural': 'Преимущества номер один',
            },
        ),
        migrations.CreateModel(
            name='AdvantagesTwoTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('info', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='AdvantagesTwo/', verbose_name='Фотография')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adventagess', to='secondary.advantagestwo')),
            ],
            options={
                'unique_together': {('settings', 'title', 'info', 'image')},
            },
        ),
    ]
