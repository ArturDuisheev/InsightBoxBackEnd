from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

# TODO: Промокод создается вместе с юзером, переместите модель промокода в account и пересмотрите архитектуру и
# надобность приложения administration. ;-)
class CreatePaymentRequestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        pass
