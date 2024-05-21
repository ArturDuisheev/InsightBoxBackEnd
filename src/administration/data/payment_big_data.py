import json
import random

from rest_framework import serializers

from core.config.helper.env_reader import env

from administration.models.PaymentModel import Package, Payment
from administration.api.serializers import PackageSerializer

serializer = PackageSerializer()

"""BEGIN PAYMENT DATA"""
api_url: str = 'https://securepay.tinkoff.ru/v2/Init'  #TODO: поместить в .env

terminal_key = env('TINKOFF_TERMINAL_KEY')

terminal_password = env('TINKOFF_TERMINAL_PASSWORD')

merchant_token = env('TINKOFF_MERCHANT_TOKEN')

api_url_for_status = f'https://securepay.tinkoff.ru/v2/GetState'

payment_data: json = {
    'TerminalKey': terminal_key,
    'Password': terminal_password,
    'Amount': 0,
    'OrderId': random.randint(1000, 99999),
    'Description': 'Оплата подписки',
    'Token': merchant_token,
    'DATA': {
        "Phone": "+71234567890",
        "Email": "a@test.com"
    },
    "Receipt": {
        "Email": "a@test.ru",
        "Phone": "+79031234567",
        "Taxation": "osn",
        # TODO: Поменять эту надпись на иттерцию
        "Items": [],

    }
}

payment_status_data = {
            "TerminalKey": terminal_key,
            "PaymentId": 0,
            "Token": merchant_token,
        }

RECCURENT_DATA = {
    "TerminalKey": env('TINKOFF_TERMINAL_KEY'),
    "PaymentId": random.randint(1000, 9999),
    "RebillId": random.randint(1000, 9999),
    "Token": merchant_token,
    "SendEmail": True,
    "InfoEmail": None,
}
"""END PAYMENT DATA"""
