from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from administration.api import serializers as admin_ser
from administration import services as admin_service


class PaymentRequestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        admin_service.create_payment_request(request=request)
        return Response('success', status=status.HTTP_200_OK)
            

    # def get(self, request, *args, **kwargs):
    #     return admin_service.check_payment_status()
