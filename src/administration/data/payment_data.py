import random

from rest_framework import serializers 

from core.config.helper.env_reader import env

from administration.models.PaymentModel import Package, Payment

"""BEGIN PAYMENT DATA"""
api_url: str = 'https://securepay.tinkoff.ru/v2/Init'#TODO: поместить в .env

terminal_key = env('TINKOFF_TERMINAL_KEY')

terminal_password = env('TINKOFF_TERMINAL_PASSWORD')

merchant_token = env('TINKOFF_MERCHANT_TOKEN')

api_url_for_status = f'https://securepay.tinkoff.ru/v2/TinkoffPay/terminals/{terminal_key}/status'

payment_data: dict = {
    'TerminalKey': terminal_key,
    'Password': terminal_password,
    'Amount': 14000,
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
"Items": "This is my happy birthday motherfuckers, salut!", 

}
}
"""END PAYMENT DATA"""

