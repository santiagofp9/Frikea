# Generated by Django 2.2.10 on 2020-02-27 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20200227_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='iemeges/'),
        ),
    ]