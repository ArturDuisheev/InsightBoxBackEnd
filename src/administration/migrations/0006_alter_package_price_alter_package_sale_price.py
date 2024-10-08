# Generated by Django 4.2.6 on 2024-05-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_alter_payment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.DecimalField(decimal_places=6, help_text='В рублях ₽', max_digits=12, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='package',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True, verbose_name='Стоимость со скидкой'),
        ),
    ]
