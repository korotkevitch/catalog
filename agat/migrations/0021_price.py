# Generated by Django 3.2.1 on 2021-05-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agat', '0020_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Название в шапке')),
                ('subtitle', models.CharField(blank=True, max_length=70, verbose_name='Подзаголовок перед текстом')),
                ('price_item', models.CharField(blank=True, max_length=70, verbose_name='Текстовый пункт прайса')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('image', models.FileField(blank=True, upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Прайс-лист',
                'verbose_name_plural': 'Прайс-лист',
            },
        ),
    ]
