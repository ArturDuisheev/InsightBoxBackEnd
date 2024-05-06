# Generated by Django 4.2.6 on 2024-05-03 10:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_esuser_promocode_alter_esuser_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esuser',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('792490e1-0255-4442-853c-196121acf7b1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]