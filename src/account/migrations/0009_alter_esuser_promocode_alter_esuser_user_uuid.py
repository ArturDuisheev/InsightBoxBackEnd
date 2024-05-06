# Generated by Django 4.2.6 on 2024-05-03 11:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_esuser_promocode_alter_esuser_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esuser',
            name='promocode',
            field=models.CharField(default='3Q5Q3Q0', max_length=10, unique=True, verbose_name='Промокод'),
        ),
        migrations.AlterField(
            model_name='esuser',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('f2bfeaa6-5790-454f-ac87-3c682b32ec7e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
