from rest_framework import serializers

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from rest_framework_simplejwt.serializers import TokenObtainSerializer, api_settings, update_last_login
from rest_framework_simplejwt.tokens import RefreshToken

from account import models as acc_mod


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('user_uuid', 'email', 'password', )

from typing import Dict, Any
from rest_framework_simplejwt.tokens import RefreshToken

class CustomTokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["user_uuid"] = str(self.user.user_uuid)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class ContactSetting(serializers.ModelSerializer):
    class Meta:
        model = acc_mod.ContactInSettings
        fields = '__all__'