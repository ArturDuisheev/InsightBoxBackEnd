# Generated by Django 4.2.6 on 2024-05-09 14:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_esuser_promocode_alter_esuser_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esuser',
            name='promocode',
            field=models.CharField(default='4A7A7A8', max_length=10, unique=True, verbose_name='Промокод'),
        ),
        migrations.AlterField(
            model_name='esuser',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('e1047214-7b24-46b2-aec7-e2e419d88b8b'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]