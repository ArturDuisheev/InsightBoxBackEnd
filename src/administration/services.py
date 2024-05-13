import requests
import logging
import random

from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework import status

from administration.models import PaymentModel as pay_mod
from administration.data import payment_data as pay_var

logger = logging.getLogger(__name__)

def create_payment_request(request):
    user = request.user
    amount = pay_var.payment_data["Amount"]
    # payment_status = pay_var.payment_data['Status']
    order_id = pay_var.payment_data['OrderId']
    print("amount:", amount)
    responce = requests.post(pay_var.api_url, json=pay_var.payment_data)
    print("json", responce.json())

    print('запрос: ', responce)
#json {'Success': True, 'ErrorCode': '0', 'TerminalKey': '1693924570978DEMO', 'Status': 'NEW', 'PaymentId': '4383404579', 'OrderId': '123', 'Amount': 14000, 'PaymentURL': 'https://securepayments.tinkoff.ru/FxmGVumH'}
    if user.balance < amount:
            raise {'message': 'На вашем балансе не достаточно средств для совершения платежа'}
    if responce.json()['Success'] is True:
        payment_url = responce.json()['PaymentURL']
        print("url: ", payment_url)

        pay_mod.Payment.objects.create(
            user=user,
            order_id=order_id,
            payment_amount=amount,
            status='ХХХ',
        )

        user.balance - amount
        return redirect(payment_url) if redirect(payment_url) is True else print('True')
            
    
    else:
        return ''.join(responce.json()['Message'] + '' + responce.json()['Details'])
    

def check_payment_status():
     pass
    # responce = requests.get(pay_var.api_url_for_status)
    # try:

    #     if responce.json()['Success'] is True:
    #         return Response(responce.json()['Message'], status=status.HTTP_200_OK)
        
    # except Exception as e:

    #     logger.debug(f'error creating payment, error: {e}')
    #     return Response(responce.json()['Message']['ErrorCode']['Details'], status=status.HTTP_400_BAD_REQUEST)


    
        


        