# Generated by Django 4.2.6 on 2024-05-14 10:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meditation', '0004_contactinsettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metaphoricalсards',
            name='likes',
        ),
        migrations.AddField(
            model_name='metaphoricalсards',
            name='likes',
            field=models.ManyToManyField(related_name='like_user', to=settings.AUTH_USER_MODEL, verbose_name='Лайки'),
        ),
    ]
