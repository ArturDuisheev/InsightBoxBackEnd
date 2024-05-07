import requests
import logging

from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework import status

from administration.models import PaymentModel as pay_mod
from administration.data import payment_data as pay_var

logger = logging.getLogger(__name__)

def create_payment_request(request):
    user = request.user
    responce = requests.post(pay_var.api_url, json=pay_var.payment_data)
    try:
        if responce.json()['Success']:
            payment_url = responce.json()['PaymentURL']

            pay_mod.Payment.objects.create(
                id=pay_var.payment_data["OrderId"].value,
                user=request.user,
                payment_amount=pay_var.payment_data["Amount"].value,
            )
            user.balance - int(pay_var.payment_data["Amount"].value)
            return redirect(payment_url)
        elif user.balance < int(pay_var.payment_data["Amount"].value):
            return Response({'message': 'На вашем балансе не достаточно средств для совершения платежа'}, 
                            status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        logger.debug(f'error creating payment, error: {e}')
    
    else:
        return responce.json()['Message'] + '' + responce.json()['Details']
    

def check_payment_status(request):
    responce = requests.get(pay_var.api_url_for_status)
    try:

        if responce.json()['Success'] is True:
            return Response(responce.json()['Message'], status=status.HTTP_200_OK)
        
    except Exception as e:

        logger.debug(f'error creating payment, error: {e}')
        return Response(responce.json()['Message']['ErrorCode']['Details'], status=status.HTTP_400_BAD_REQUEST)


    
        


        