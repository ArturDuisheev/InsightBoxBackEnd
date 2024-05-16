import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from account import models as acc_mod


class Package(models.Model):
    name = models.CharField(
        _('Наименование пакета'),
        max_length=120
    )
    how_month = models.CharField(
        _('На сколько месяцев?'),
        help_text='Пример: 12 месяцев, 6 месяцев и тд',
        max_length=20
    )
    price = models.PositiveIntegerField(
        _('Стоимость'),
        help_text='В рублях ₽'
    )
    sale_price = models.PositiveIntegerField(
        _('Стоимость со скидкой'),
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        have_sale = 'скидки нет' if self.sale_price is not None else 'скидка есть'
        return f'Пакет: {self.name}, стоимость пакета: {self.price}, {have_sale}'

    class Meta:
        verbose_name = _('Добавление пакета')
        verbose_name_plural = _('Добавление пакетов')


class Payment(models.Model):
    order_id = models.PositiveIntegerField(
        _('Номер заказа'),
        primary_key=True,
        editable=False,
    )
    payment_id = models.PositiveIntegerField(
        _('Номер платежа'),
        editable=False,
    )
    user = models.ForeignKey(
        acc_mod.EsUser,
        verbose_name=_('Пользователь'),
        on_delete=models.SET_NULL,
        related_name='user_payment',
        null=True
    )
    payment_amount = models.PositiveIntegerField(
        _('Сумма оплаты'),
    )
    package = models.ForeignKey(
        Package,
        on_delete=models.SET_NULL,
        related_name='package_payment',
        verbose_name=_('Пакеты'),
        null=True
    )
    created_at = models.DateTimeField(
        _('Дата оплаты'),
        auto_now_add=True
    )
    status = models.CharField(
        _('Статус'),
        max_length=120,
        editable=False,
    )

    def __str__(self) -> str:
        return f'Номер заказа: {self.order_id}, ID пользователя: {self.user.user_uuid}, сумма оплаты: {self.payment_amount}'

    class Meta:
        verbose_name = _('История оплаты')
        verbose_name_plural = verbose_name
