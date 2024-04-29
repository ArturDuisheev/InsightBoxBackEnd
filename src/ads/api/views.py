from rest_framework import generics, permissions

from ads.api import serializers as ad_ser
from ads import models as ad_mod

class AdListAPIView(generics.ListAPIView):
    queryset = ad_mod.AdModel.objects.all()
    serializer_class = ad_ser.AdSerializer
    permission_classes = [permissions.AllowAny]
