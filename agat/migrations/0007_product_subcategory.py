# Generated by Django 3.2.1 on 2021-05-15 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agat', '0006_remove_product_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(blank=True, max_length=30, verbose_name='Подкатегория'),
        ),
    ]
