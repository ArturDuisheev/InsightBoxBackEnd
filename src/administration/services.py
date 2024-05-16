import requests
import logging
import random

from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.response import Response

from administration.data.payment_big_data import terminal_key, merchant_token
from administration.models import PaymentModel as pay_mod
from administration.data import payment_big_data as pay_var
from administration.api import serializers as pay_ser

logger = logging.getLogger(__name__)


class PaymentService:
    def __init__(self, api_url, payment_data, terminal_key, merchant_token):
        self.api_url = api_url
        self.payment_data = payment_data
        self.terminal_key = terminal_key
        self.merchant_token = merchant_token

    def create_payment_request(self, request, amount, package):
        user = request.user
        package_serializer = pay_ser.PackageSerializer(package)

        data = package_serializer.data
        self.payment_data["Amount"] = amount
        self.payment_data['Receipt']['Items'].append({
            'Name': data['name'],
            'Price': data['price'],
            'Quantity': 1,
            'Amount': data['price'],
            'Tax': "vat10",
        })

        response = requests.post(self.api_url, json=self.payment_data)
        response_data = response.json()

        print("Response:", response_data)
        print("Payment data:", self.payment_data)

        if user.balance < self.payment_data["Amount"]:
            return JsonResponse({'message': 'Not enough balance for this payment'}, status=400)

        if response_data.get('Success', False):
            payment_url = response_data.get('PaymentURL', '')

            pay_mod.Payment.objects.create(
                user=user,
                order_id=self.payment_data['OrderId'],
                payment_id=response_data['PaymentId'],
                payment_amount=self.payment_data["Amount"],
                package=data.get('id'),
                status='New',
            )

            user.balance -= self.payment_data["Amount"]
            user.save()

            return Response(response_data, status=200)
        else:
            error_message = response_data.get('Message', '')
            error_details = response_data.get('Details', '')
            return JsonResponse({'message': f'{error_message}. {error_details}'}, status=400)

    def check_payment_status(self, payment_id, api_status_url, payment_status_data):
        payment_status_data['PaymentId'] = payment_id
        a = requests.post(api_status_url, json=payment_status_data)
        print(a.json())
        return a




# responce = requests.get(pay_var.api_url_for_status)
# try:

#     if responce.json()['Success'] is True:
#         return Response(responce.json()['Message'], status=status.HTTP_200_OK)

# except Exception as e:

#     logger.debug(f'error creating payment, error: {e}')
#     return Response(responce.json()['Message']['ErrorCode']['Details'], status=status.HTTP_400_BAD_REQUEST)


# def reccurent_payment(request: str, amount: int, duration: str) -> str:
#     responce = requests.post(x)
