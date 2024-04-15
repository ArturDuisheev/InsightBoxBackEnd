from account.models import EsUser
from django.db.models import Q


class AuthBackend(object):
    supports_objects_permissions = True
    supports_annonymous_user = False
    supports_inactive_user = True

    def get_user(self, user_uuid):
        try:
            return EsUser.objects.get(pk=user_uuid)
        except EsUser.DoesNotExist:
            return None
        
    
    def authenticate(self, email, password):
        try:
            user = EsUser.objects.get(
            email=email
            )
        except EsUser.DoesNotExist:
            return None
        
        return user if user.check_password(password) else None