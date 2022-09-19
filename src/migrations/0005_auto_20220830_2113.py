# Generated by Django 3.1.2 on 2022-08-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='sub_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]