# Generated by Django 3.2.1 on 2021-05-14 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agat', '0003_category_product_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]