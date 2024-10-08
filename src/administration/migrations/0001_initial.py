# Generated by Django 4.2.6 on 2024-05-06 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Наименование пакета')),
                ('how_month', models.CharField(help_text='Пример: 12 месяцев, 6 месяцев и тд', max_length=20, verbose_name='На сколько месяцев?')),
                ('price', models.DecimalField(decimal_places=3, help_text='В рублях ₽', max_digits=4, verbose_name='Стоимость')),
                ('sale_price', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True, verbose_name='Стоимость со скидкой')),
            ],
            options={
                'verbose_name': 'Добавление пакета',
                'verbose_name_plural': 'Добавление пакетов',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='Дата оплаты')),
                ('payment_amount', models.DecimalField(decimal_places=3, max_digits=4, verbose_name='Сумма оплаты')),
                ('status', models.CharField(choices=[('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED'), ('IN_PROCCESING', 'IN_PROCCESESING')], default='IN_PROCCESING', max_length=120, verbose_name='Статус')),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='package_payment', to='administration.package', verbose_name='Пакеты')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_payment', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'История оплаты',
                'verbose_name_plural': 'История оплаты',
            },
        ),
    ]
