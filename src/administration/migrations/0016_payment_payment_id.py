# Generated by Django 4.2.6 on 2024-05-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0015_alter_package_price_alter_package_sale_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_id',
            field=models.PositiveIntegerField(default=1, editable=False, verbose_name='Номер платежа'),
            preserve_default=False,
        ),
    ]
