# Generated by Django 4.2.6 on 2024-05-13 10:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_alter_esuser_promocode_alter_esuser_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esuser',
            name='promocode',
            field=models.CharField(default='4O4O4O5', max_length=10, unique=True, verbose_name='Промокод'),
        ),
        migrations.AlterField(
            model_name='esuser',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('47a0144b-3dba-459c-977c-b09bb8ebbfb8'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]