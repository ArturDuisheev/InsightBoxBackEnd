from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from meditation.api import serializers as med_ser
from meditation import models as med_mod
from meditation import services as med_service


class MeditationListCreateAPIView(generics.ListCreateAPIView):
    queryset = med_mod.Meditation.objects.all()
    serializer_class = med_ser.MeditationSerializer
    # permission_classes = None # TODO: Добавить permissions после тестов


class MeditationLikeAPIView(APIView):

    def get(self, request, *args, **kwargs):
        meditation_id = kwargs.get('id')
        favorite_count = med_service.get_favorite_count_meditation(meditation_id)
        if favorite_count is None:
            return Response({'message': 'Медитация не найдена'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'favorite_count': favorite_count}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        meditation_id = kwargs.get('pk')
        success, message = med_service.toggle_favorite_status_meditation(meditation_id, request.user)
        if not success:
            return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': message}, status=status.HTTP_201_CREATED)


class ContactSettingListAPiView(generics.ListAPIView):
    queryset = med_mod.ContactInSettings.objects.all()
    serializer_class = med_ser.ContactSettingSerializer


class MetaforicalCardListCreateAPIVew(generics.ListCreateAPIView):
    queryset = med_mod.MetaphoricalСards.objects.all()
    serializer_class = med_ser.MetaforicalCardSerializer


class MetaforicalCardLikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        card_id = kwargs.get('pk')
        favorite_count = med_service.get_favorite_count(card_id)
        if favorite_count is None:
            return Response({'message': 'Карта не найдена'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'favorite_count': favorite_count}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        card_id = kwargs.get('pk')
        success, message = med_service.toggle_favorite_status(card_id, request.user)
        if not success:
            return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': message}, status=status.HTTP_201_CREATED)
