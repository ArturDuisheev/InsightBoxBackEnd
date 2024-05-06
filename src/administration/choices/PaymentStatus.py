from django.db.models import TextChoices

from django.utils.translation import gettext_lazy as _

class PayStatus(TextChoices):
    APPROVED = 'APPROVED', _('APPROVED')
    REJECTED = 'REJECTED', _('REJECTED')
    IN_PROCCESING = 'IN PROCCESING', _('IN PROCCESESING')

