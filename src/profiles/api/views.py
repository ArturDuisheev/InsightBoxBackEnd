from rest_framework import generics

from profiles import models as prof
from profiles.api import serializers as prof_ser


class ProfileListAPIView(generics.ListAPIView):
    queryset = prof.Profile.objects.all()
    serializer_class = prof_ser.ProfileSerializer

class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = prof.Profile.objects.all()
    serializer_class = prof_ser.ProfileSerializer
    lookup_field = 'user_id'