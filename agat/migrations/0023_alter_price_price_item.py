# Generated by Django 3.2.1 on 2021-05-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agat', '0022_auto_20210519_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price_item',
            field=models.CharField(blank=True, max_length=200, verbose_name='Тариф'),
        ),
    ]
