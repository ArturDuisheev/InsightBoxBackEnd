# Generated by Django 4.2.6 on 2024-05-15 13:48

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='HitCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.PositiveIntegerField(verbose_name='Понедельник')),
                ('tuesday', models.PositiveIntegerField(verbose_name='Вторник')),
                ('wednesday', models.PositiveIntegerField(verbose_name='Среда')),
                ('thursday', models.PositiveIntegerField(verbose_name='Четверг')),
                ('friday', models.PositiveIntegerField(verbose_name='Пятница')),
                ('saturday', models.PositiveIntegerField(verbose_name='Суббота')),
                ('sunday', models.PositiveIntegerField(verbose_name='Воскресенье')),
            ],
        ),
        migrations.CreateModel(
            name='EsUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_uuid', models.UUIDField(default=uuid.UUID('b6ae4f99-d3bf-45b1-8b0f-ad7b65012501'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('username', models.CharField(max_length=120, unique=True, verbose_name='username')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Доступ к админке')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный пользователь')),
                ('is_verified', models.BooleanField(default=True)),
                ('balance', models.DecimalField(decimal_places=6, default=0, max_digits=12, verbose_name='Баланс юзера')),
                ('promocode', models.CharField(default='1V9V0V7', max_length=10, unique=True, verbose_name='Промокод')),
                ('is_premium', models.BooleanField(default=False, verbose_name='Премиум?')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'unique_together': {('email',)},
            },
        ),
    ]
