# Generated by Django 2.2.10 on 2020-03-04 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_auto_20200227_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]