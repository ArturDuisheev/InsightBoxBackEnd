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

api_url_for_status = f'https://securepay.tinkoff.ru/v2/TinkoffPay/terminals/{terminal_key}/status'

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

PAYMENT_STATUS = {
    "TerminalKey": terminal_key,
    "PaymentId": 13660,
    "Token": merchant_token,
}

RECCURENT_DATA = {
    "TerminalKey": env('TINKOFF_TERMINAL_KEY'),
    "PaymentId": 700001702044,
    "RebillId": "145919",
    "Token": "f5a3be479324a6d3a4d9efa0d02880b77d04a91758deddcbd9e752a6df97cab5",
    "IP": "2011:0db8:85a3:0101:0101:8a2e:0370:7334",
    "SendEmail": True,
    "InfoEmail": "customer@test.com"
}
"""END PAYMENT DATA"""
