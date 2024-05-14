import requests
import logging
import random

from django.http import JsonResponse
from django.shortcuts import redirect

from administration.models import PaymentModel as pay_mod
from administration.data import payment_data as pay_var
from administration.api import serializers as pay_ser


logger = logging.getLogger(__name__)


def create_payment_request(request, amount, package):
    user = request.user
    package_serializer = pay_ser.PackageSerializer(package)

    # Обновление данных платежа
    data = package_serializer.data
    pay_var.payment_data["Amount"] = amount
    pay_var.payment_data['Receipt']['Items'].append({
        'Name': data['name'],
        'Price': data['price'],
        'Quantity': 1,
        'Amount': data['price'],
        'Tax': "vat10",
    })

    responce = requests.post(pay_var.api_url, json=pay_var.payment_data)
    print("resp", responce.json())
    print("data", pay_var.payment_data)

    if user.balance < pay_var.payment_data["Amount"]:
        return JsonResponse({'message': 'На вашем балансе не достаточно средств для совершения платежа'}, status=400)

    if responce.json()['Success']:
        payment_url = responce.json()['PaymentURL']

        # Создание записи о платеже
        pay_mod.Payment.objects.create(
            user=user,
            order_id=pay_var.payment_data['OrderId'],
            payment_amount=pay_var.payment_data["Amount"],
            package=data.get('id'),
            status='New',
        )

        # Обновление баланса пользователя
        user.balance -= pay_var.payment_data["Amount"]
        user.save()

        return redirect(payment_url)
    else:
        error_message = responce.json()['Message']
        error_details = responce.json().get('Details', '')
        return JsonResponse({'message': f'{error_message}. {error_details}'}, status=400)


def check_payment_status():
    pass
# responce = requests.get(pay_var.api_url_for_status)
# try:

#     if responce.json()['Success'] is True:
#         return Response(responce.json()['Message'], status=status.HTTP_200_OK)

# except Exception as e:

#     logger.debug(f'error creating payment, error: {e}')
#     return Response(responce.json()['Message']['ErrorCode']['Details'], status=status.HTTP_400_BAD_REQUEST)
