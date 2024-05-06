from rest_framework import generics

from meditation.api import serializers as med_ser
from meditation import models as med_mod

class MeditationListCreateAPIView(generics.ListCreateAPIView):
    queryset = med_mod.Meditation.objects.all()
    serializer_class = med_ser.MeditationSerializer
    # permission_classes = None # TODO: Добавить permissions после тестов

class MeditationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = med_mod.Meditation.objects.all()
    serializer_class = med_ser.MeditationSerializer

class ContactSettingListAPiView(generics.ListAPIView):
    queryset = med_mod.ContactInSettings.objects.all()
    serializer_class = med_ser.ContactSettingSerializer

