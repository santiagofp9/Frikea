# Generated by Django 2.2.10 on 2020-02-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_auto_20200227_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='static/iemeges/'),
        ),
    ]
