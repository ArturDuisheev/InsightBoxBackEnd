from django.dispatch import receiver
from djoser.signals import user_registered

from profiles.models import Profile


@receiver(user_registered)
def create_profile(sender, request, user, **kwargs):
    Profile.objects.create(
        user=user
    )
    print(user)