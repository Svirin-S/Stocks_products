# Generated by Django 4.1.4 on 2022-12-29 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Склад', 'verbose_name_plural': 'Склады'},
        ),
    ]
