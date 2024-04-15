from django.db import models

from django.utils.translation import gettext_lazy as _

from account.models import EsUser


class Profile(models.Model):
    user = models.OneToOneField(
        EsUser,
        related_name='profile_user',
        verbose_name=_('Профиль'),
        on_delete=models.CASCADE
        )
    name = models.CharField(
        _('Имя'),
        max_length=100,
        blank=True,
        null=True
    )
    surname = models.CharField(
        _('Фамилия'),
        max_length=120,
        blank=True,
        null=True
    )


    def __str__(self) -> str:
        return f'ID: {self.user.user_uuid}, Имя: {self.name}'
    
    class Meta:
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профили')


    
