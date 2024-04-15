# Generated by Django 4.2.6 on 2024-04-11 06:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='esuser',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='esuser',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('99c1807b-b892-447a-89f6-db7d416a2b31'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
