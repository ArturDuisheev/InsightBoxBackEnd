from rest_framework import serializers

from ads import models as ad_mod

class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = ad_mod.AdModel
        fields = ('id', 'title', 'quote', 'preority', 'image')