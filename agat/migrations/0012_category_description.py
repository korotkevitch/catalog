# Generated by Django 3.2.1 on 2021-05-17 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agat', '0011_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=70, verbose_name='Описание'),
        ),
    ]
