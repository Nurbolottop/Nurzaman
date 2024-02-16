# Generated by Django 5.0 on 2023-12-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0017_alter_apartment_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название блока')),
            ],
            options={
                'verbose_name': 'Добавить блок',
                'verbose_name_plural': 'Добавить блок',
            },
        ),
        migrations.AddField(
            model_name='apartment',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]
