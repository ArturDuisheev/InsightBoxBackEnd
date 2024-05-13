# Generated by Django 4.2.6 on 2024-05-09 14:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_alter_esuser_balance_alter_esuser_promocode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esuser',
            name='promocode',
            field=models.CharField(default='6O2O9O1', max_length=10, unique=True, verbose_name='Промокод'),
        ),
        migrations.AlterField(
            model_name='esuser',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('b2500cac-5650-441e-90cd-3b02325f288d'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
