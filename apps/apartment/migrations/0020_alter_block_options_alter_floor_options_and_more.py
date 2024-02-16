# Generated by Django 5.0 on 2023-12-30 00:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0019_apartment_block_alter_apartment_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'verbose_name': 'Добавить Блок', 'verbose_name_plural': 'Добавить Блоки'},
        ),
        migrations.AlterModelOptions(
            name='floor',
            options={'verbose_name': 'Добавить Этаж', 'verbose_name_plural': 'Добавить Этажи'},
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='block',
        ),
        migrations.AddField(
            model_name='floor',
            name='block',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apartment.block', verbose_name='Выбрать блок'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='floor',
            name='title',
            field=models.IntegerField(default=0, verbose_name='этаж'),
        ),
    ]