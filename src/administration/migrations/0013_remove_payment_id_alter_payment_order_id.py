# Generated by Django 4.2.6 on 2024-05-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0012_remove_payment_payment_uuid_payment_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='id',
        ),
        migrations.AlterField(
            model_name='payment',
            name='order_id',
            field=models.PositiveIntegerField(editable=False, primary_key=True, serialize=False, verbose_name='Номер заказа'),
        ),
    ]