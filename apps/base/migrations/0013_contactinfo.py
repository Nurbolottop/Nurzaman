# Generated by Django 5.0 on 2023-12-28 22:15

import ckeditor.fields
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_settingssoc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='gallery/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Заказать обратный Звонок',
                'verbose_name_plural': 'Заказать обратный Звонок',
            },
        ),
    ]
