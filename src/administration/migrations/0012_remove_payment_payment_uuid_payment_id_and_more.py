# Generated by Django 4.2.6 on 2024-05-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0011_alter_payment_payment_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_uuid',
        ),
        migrations.AddField(
            model_name='payment',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1131, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='order_id',
            field=models.PositiveIntegerField(default=1231, verbose_name='Номер заказа'),
            preserve_default=False,
        ),
    ]
