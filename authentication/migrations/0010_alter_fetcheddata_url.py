# Generated by Django 4.1.7 on 2023-03-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_fetcheddata_is_downloaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fetcheddata',
            name='url',
            field=models.URLField(max_length=255, unique=True),
        ),
    ]
