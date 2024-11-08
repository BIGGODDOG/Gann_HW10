# Generated by Django 5.1.1 on 2024-11-03 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('specialization', models.CharField(max_length=100, verbose_name='Специализация')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('website', models.URLField(blank=True, verbose_name='Веб-сайт')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Контактный телефон')),
            ],
        ),
    ]
