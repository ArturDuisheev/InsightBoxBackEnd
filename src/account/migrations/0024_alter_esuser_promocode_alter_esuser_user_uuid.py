# Generated by Django 4.2.6 on 2024-05-09 14:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_alter_esuser_promocode_alter_esuser_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esuser',
            name='promocode',
            field=models.CharField(default='5E1E0E3', max_length=10, unique=True, verbose_name='Промокод'),
        ),
        migrations.AlterField(
            model_name='esuser',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('d11d5b72-b8f0-4f41-a927-41c2c4f54247'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
