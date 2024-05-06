import requests
import logging

from django.shortcuts import redirect

from administration.models import PaymentModel as pay_mod
from administration.data import payment_data as pay_var

logger = logging.getLogger(__name__)

def create_payment_request(request):
    responce = requests.post(pay_var.api_url, json=pay_var.payment_data)
    try:
        if responce.json()['Success']:
            payment_url = responce.json()['PaymentURL']

            pay_mod.Payment.objects.create(
                id=pay_var.payment_data["OrderId"].value,
                user=request.user,
                payment_amount=pay_var.payment_data["Amount"].value,
            )

            return redirect(payment_url)
    except Exception as e:
        logger.debug(f'error creating payment, error: {e}')
    
    else:
        return responce.json()['Message'] + '' + responce.json()['Details']
    

def check_payment_status(request, payment_id):
    pass
    
        


        