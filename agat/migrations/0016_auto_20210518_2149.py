# Generated by Django 3.2.1 on 2021-05-18 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agat', '0015_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('image', models.FileField(blank=True, upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.AlterModelOptions(
            name='catalog',
            options={'verbose_name': 'Каталог', 'verbose_name_plural': 'Каталог'},
        ),
    ]