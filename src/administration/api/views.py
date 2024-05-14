import json

from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from administration.api import serializers as admin_ser
from administration import services as admin_service
from administration.models import PaymentModel as admin_mod


class PaymentRequestAPIView(APIView):

    # def post(self, request, *args, **kwargs):
    #     serializer = admin_ser.PaymentSerializer(data=request.data)
    #
    #     if serializer.is_valid(raise_exception=True):
    #         package = serializer.validated_data['package']
    #
    #         admin_service.create_payment_request(request=request, amount=package.price, package=package)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, *args, **kwargs):
    #     return admin_service.check_payment_status()
    @swagger_auto_schema(request_body=admin_ser.PaymentSerializer, responses={200: 'OK', 400: 'Bad Request'})
    def post(self, request):
        data = request.data
        serializer = admin_ser.PaymentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            package_id = serializer.validated_data['package']
            shit = admin_mod.Package.objects.get(id=package_id)
            admin_service.create_payment_request(request=request, amount=shit.price, package=shit)
            print('done')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


