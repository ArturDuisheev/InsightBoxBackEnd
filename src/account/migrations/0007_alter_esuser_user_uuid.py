# Generated by Django 4.2.6 on 2024-05-03 10:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_esuser_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esuser',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('f7b3616e-0a72-4282-a6c0-def566bda250'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]