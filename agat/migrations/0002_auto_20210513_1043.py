# Generated by Django 3.2.1 on 2021-05-13 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]