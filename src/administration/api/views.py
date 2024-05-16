from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from administration.api import serializers as admin_ser
from administration import services as admin_service
from administration.models import PaymentModel as admin_mod
from administration.data import payment_big_data as pay_var


class PaymentRequestAPIView(APIView):
    @swagger_auto_schema(request_body=admin_ser.PaymentSerializer, responses={200: 'OK', 400: 'Bad Request'})
    def post(self, request):
        serializer = admin_ser.PaymentSerializer(data=request.data)

        if serializer.is_valid():
            package_id = serializer.validated_data.get('package')
            try:
                package = admin_mod.Package.objects.get(id=package_id)
            except admin_mod.Package.DoesNotExist:
                return Response({'message': 'Package not found'}, status=status.HTTP_400_BAD_REQUEST)

            payment_service = admin_service.PaymentService(
                api_url=pay_var.api_url,
                payment_data=pay_var.payment_data,
                terminal_key=pay_var.terminal_key,
                merchant_token=pay_var.merchant_token,
            )
            response = payment_service.create_payment_request(request=request, amount=package.price, package=package)
            print('done')
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetPaymentStatusAPIView(APIView):
    serializer_class = admin_ser.PaymentStatusSerializer

    @swagger_auto_schema(responses={200: admin_ser.PaymentStatusSerializer(), 400: 'Bad Request'})
    def post(self, request, payment_id):
        data = {'payment_id': payment_id}

        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            payment_id = serializer.validated_data['payment_id']
            print("payment", payment_id)

            payment_service = admin_service.PaymentService(
                api_url=pay_var.api_url_for_status,
                payment_data=pay_var.payment_status_data,
                terminal_key=pay_var.terminal_key,
                merchant_token=pay_var.merchant_token,
            )

            response = payment_service.check_payment_status(
                payment_id=payment_id,
                api_status_url=payment_service.api_url,
                payment_status_data=payment_service.payment_data
            )
            print()

            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
