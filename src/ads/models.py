from django.db import models

from django.utils.translation import gettext_lazy as _ 

class AdModel(models.Model):
    title = models.CharField(
        _('Заголовок'),
        max_length=50,
        blank=True,
        null=True
    )
    quote = models.CharField(
        _('Цитата снизу'),
        max_length=70,
        blank=True,
        null=True
    )
    preority = models.BooleanField(
        _('Выставить в приоритет?'),
        default=True,
    )
    image = models.ImageField(
        _('Баннер'),
        upload_to='images/ads/'
    )

    def __str__(self) -> str:
        preority = self.preority if False else 'Да' if True else 'Нет'
        return f'реклама: {self.title}, приоритетная? {preority}'
    
    class Meta:
        verbose_name = _('Реклама')
        verbose_name_plural = verbose_name

