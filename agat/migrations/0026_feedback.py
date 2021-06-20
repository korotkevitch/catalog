# Generated by Django 3.2.1 on 2021-05-19 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agat', '0025_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('message', models.TextField(blank=True, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]