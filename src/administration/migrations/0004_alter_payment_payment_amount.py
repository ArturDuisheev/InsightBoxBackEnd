# Generated by Django 4.2.6 on 2024-05-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_alter_package_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма оплаты'),
        ),
    ]