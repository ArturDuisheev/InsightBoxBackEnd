import uuid

from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from account.api.managers import EsUserManager
from account.services.promocode import create_promocode


class HitCounter(models.Model):
    monday = models.PositiveIntegerField(
        _('Понедельник')
    )
    tuesday = models.PositiveIntegerField(
        _('Вторник')
    )
    wednesday = models.PositiveIntegerField(
        _('Среда')
    )
    thursday = models.PositiveIntegerField(
        _('Четверг')
    )
    friday = models.PositiveIntegerField(
        _('Пятница')
    )
    saturday = models.PositiveIntegerField(
        _('Суббота')
    )
    sunday = models.PositiveIntegerField(
        _('Воскресенье')
    )


class EsUser(AbstractUser, PermissionsMixin):
    user_uuid = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4()
    )
    email = models.EmailField(_('Почта'), unique=True)
    username = models.CharField(_('username'), max_length=120, unique=True)
    # phone = PhoneNumberField()

    is_superuser = models.BooleanField(
        _('Доступ к админке'),
        default=False
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        _('Активный пользователь'),
        default=True,
    )
    is_verified = models.BooleanField(
        default=True
    )
    balance = models.DecimalField(
        _('Баланс юзера'),
        max_digits=12,
        decimal_places=6,
        default=0
    )
    promocode = models.CharField(
        max_length=10,
        # editable=False,
        verbose_name=_('Промокод'),
        unique=True,
        default=create_promocode()
    )
    is_premium = models.BooleanField(
        _('Премиум?'),
        default=False
    )
    is_purchased_money_metaphorical_cards = models.BooleanField(
        _('Оплата за метафорические карты'),
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = EsUserManager()

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        unique_together = ('email', )

    def __str__(self):
        return f'никнейм: {self.username}, id: {self.user_uuid}'
