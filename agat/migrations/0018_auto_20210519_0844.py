# Generated by Django 3.2.1 on 2021-05-19 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agat', '0017_service_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='subtitle',
            field=models.CharField(blank=True, max_length=70, verbose_name='Подзаголовок перед текстом'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(blank=True, max_length=50, verbose_name='Название в шапке'),
        ),
    ]