from rest_framework import serializers

from profiles import models as acc_prof

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField('get_email')
    username = serializers.SerializerMethodField('get_username')   


    class Meta:
        model = acc_prof.Profile
        fields = ('id', 'user', 'name', 'surname', 'email', 'username')

    def get_email(self, obj):
        return obj.user.email
    
    def get_username(self, obj):
        return obj.user.username
    




