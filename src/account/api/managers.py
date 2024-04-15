from django.contrib.auth.models import BaseUserManager


class EsUserManager(BaseUserManager):
    def _create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('At least one of username, email, must be set')

        if email:
            email = self.normalize_email(email)


        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verified', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(password=password, **extra_fields)
    