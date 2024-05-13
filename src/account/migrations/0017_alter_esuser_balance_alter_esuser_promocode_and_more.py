# Generated by Django 4.2.6 on 2024-05-08 12:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_alter_esuser_promocode_alter_esuser_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esuser',
            name='balance',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=12, verbose_name='Баланс юзера'),
        ),
        migrations.AlterField(
            model_name='esuser',
            name='promocode',
            field=models.CharField(default='3T4T2T7', max_length=10, unique=True, verbose_name='Промокод'),
        ),
        migrations.AlterField(
            model_name='esuser',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('860469f7-725b-4319-b567-0c243de49c5a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
