# Generated by Django 4.2.6 on 2024-05-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0014_alter_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.PositiveIntegerField(help_text='В рублях ₽', verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='package',
            name='sale_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Стоимость со скидкой'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.PositiveIntegerField(verbose_name='Сумма оплаты'),
        ),
    ]