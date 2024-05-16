import requests
import logging

from django.http import JsonResponse
from rest_framework.response import Response

from administration.models import PaymentModel as pay_mod
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
        self.payment_data['Receipt'].update({
            'Email': user.email,
        })
        self.payment_data['DATA'].update({
            'Email': user.email
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
                package=package,
                status=response_data['Status'],
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
        status_url = requests.post(api_status_url, json=payment_status_data)
        print(status_url.json())
        return status_url
