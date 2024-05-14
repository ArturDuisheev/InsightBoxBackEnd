from typing import Any, Dict
from rest_framework import serializers
from mutagen.mp3 import MP3

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt import serializers as jwt_ser

from meditation import models as med_mod


class CustomTokenObtainPairSerializer(jwt_ser.TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        user_uuid: str = self.user.user_uuid

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data['user_uuid'] = str(user_uuid)

        if jwt_ser.api_settings.UPDATE_LAST_LOGIN:
            jwt_ser.update_last_login(None, self.user)

        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = med_mod.Category
        fields = ('id', 'name')


class MeditationSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField('get_duration')

    class Meta:
        model = med_mod.Meditation
        fields = ('id', 'title', 'audio', 'duration', 'is_premium', 'likes')

    def get_duration(self, obj):
        return int(MP3(obj.audio).info.length / 60)


class MetaforicalCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = med_mod.MetaphoricalСards
        fields = ('id', 'image_card', 'value', 'transcript', 'advice', 'affirmation', 'likes')


class ContactSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = med_mod.ContactInSettings
        fields = '__all__'
