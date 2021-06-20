# Generated by Django 3.2.1 on 2021-05-24 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agat', '0031_auto_20210523_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Просьба позвонить',
                'verbose_name_plural': 'Просьбы позвонить',
            },
        ),
    ]
