# Generated by Django 5.0 on 2023-12-22 01:31

import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0007_euro_alter_pride_first_alter_pride_five_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название сайта')),
                ('chert', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='Choise_chert/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Сделай свой выбор',
                'verbose_name_plural': 'Сделай свой выбор',
            },
        ),
        migrations.AlterField(
            model_name='euroimage',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='euro/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='projects/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='slide/', verbose_name='Фотография'),
        ),
        migrations.CreateModel(
            name='ChoiseTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('razmer', models.CharField(max_length=255, verbose_name='Площадь')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choise_image', to='secondary.choise')),
            ],
            options={
                'unique_together': {('settings', 'title', 'razmer')},
            },
        ),
    ]
