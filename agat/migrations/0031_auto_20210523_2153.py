# Generated by Django 3.2.1 on 2021-05-23 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agat', '0030_auto_20210523_2005'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
    ]
