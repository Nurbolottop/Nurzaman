# Generated by Django 5.0 on 2024-01-03 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0026_alter_apartment_razmer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
    ]
