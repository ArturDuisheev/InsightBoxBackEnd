from django.db import models

from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

from account import models as acc_mod
from meditation.utils.compress_audio import compress_audio


class Category(models.Model):
    name = models.CharField(
        _('Категория'),
        max_length=120
    )

    def __str__(self) -> str:
        return f'Категория: {self.name}'


class Meditation(models.Model):
    title = models.CharField(
        _('Название медитации'),
        max_length=120
    )
    audio = models.FileField(
        _('Запись медитации'),
        upload_to='uploads/meditations/audio/',
        validators=[FileExtensionValidator(
            allowed_extensions=['mp3', 'ogg', 'aac', ]
        )],
        blank=True,
        null=True
    )
    duration = models.CharField(
        _('Длительность'),
        max_length=50,
        blank=True,
        null=True
    )
    # is_bronze = models.BooleanField(
    #     _('Бронза?'),
    #     default=False
    # )
    # is_silver = models.BooleanField(
    #     _('Серебро?'),
    #     default=False
    # )
    # is_premium = models.BooleanField(
    #     _('Золото?'),
    #     default=False
    # )
    likes = models.ManyToManyField(
        acc_mod.EsUser,
        related_name='meditation_likes',
        verbose_name=_('Лайки'),
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs) -> None:
        if self.audio:
            try:
                with open(self.audio.path, 'rb') as file:
                    compressed_data = compress_audio(file.read())

                with open(self.audio.path, 'wb') as file:
                    file.write(compressed_data)

            except Exception as e:
                print("Произошла ошибка при сжатии аудио:", str(e))

        super(Meditation, self).save(*args, **kwargs)

    def __str__(self):
        is_prem = 'Да' if self.is_premium else 'нет'
        return f'название: {self.title}, премиум? {is_prem}'

    class Meta:
        verbose_name = _('Медитация')
        verbose_name_plural = _('Медитации')


class MetaphoricalCard(models.Model):
    image_card = models.ImageField(
        _('Изображение карты'),
        upload_to='images/metaphorical_cards/',
        blank=True,
        null=True
    )
    video = models.FileField(
        _('Видео'),
        upload_to='videos/metaphorical_cards/'
    )
    meaning = models.TextField(
        _('Значение')
    )
    transcript = models.TextField(
        _('Расшифровка')
    )
    advice = models.TextField(
        _('Совет')
    )
    affirmation = models.TextField(
        _('Аффермация')
    )
    likes = models.ManyToManyField(
        acc_mod.EsUser,
        related_name='like_user',
        verbose_name=_('Лайки'),
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f'Карта номер: {self.id}'

    class Meta:
        verbose_name = _('Колода метафорических карт')
        verbose_name_plural = verbose_name


class MoneyMetaphoricalCard(models.Model):
    image = models.ImageField(
        _('Фото'),
        upload_to='images/money_cards/'
    )

    title = models.CharField(
        _('Заголовок'),
        max_length=120
    )
    description = models.TextField(
        _('Содержание')
    )
    meaning = models.TextField(
        _('Значение')
    )
    advice = models.TextField(
        _('Совет')
    )
    affirmation = models.TextField(
        _('Аффермация')
    )

    def __str__(self):
        return f'Денежная карта номер: {self.id}'

    class Meta:
        verbose_name = _('Денежная колода метафорических карт')
        verbose_name_plural = verbose_name


class ContactInSettings(models.Model):
    vk = models.URLField(
        _('ссылка на соц.сеть Вконтакте')
    )
    instagram = models.URLField(
        _('ссылка на соц.сеть инстаграм')
    )
    telegram = models.URLField(
        _('Телеграм')
    )
    yandex_dzen = models.URLField(
        _('Яндекс дзен')
    )
    website = models.URLField(
        _('Вебсайт')
    )

    def __str__(self) -> str:
        return f'Пакет соц.сетей #{self.id}'

    class Meta:
        verbose_name = _('Контакт приложения')
        verbose_name_plural = _('Контакты приложения')
