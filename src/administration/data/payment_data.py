from core.config.helper.env_reader import env

"""BEGIN PAYMENT DATA"""
api_url: str = env('TINKOFF_URL_API') #TODO: поместить в .env

terminal_key = env('TINKOFF_TERMINAL_KEY')

terminal_password = env('TINKOFF_TERMINAL_PASSWORD')

merchant_token = env('TINKOFF_MERCHANT_TOKEN')

api_url_for_status = f'https://securepay.tinkoff.ru/v2/TinkoffPay/terminals/{terminal_key}/status'

payment_data: dict = {
    'TerminalKey': terminal_key,
    'Password': terminal_password,
    'Amount': 13,
    'OrderId': '123',
    'Description': 'Payment request test',
    'Token': merchant_token,
    'DATA': {
        "Phone": "+71234567890",
        "Email": "a@test.com"
    },
    "Receipt": {
        "Email": "a@test.ru",
        "Phone": "+79031234567",
        "Taxation": "osn",
"Items": [
    {
        "Name": "Наименование товара 1",
        "Price": 10000,
        "Quantity": 1,
        "Amount": 10000,
        "Tax": "vat10",
        "Ean13": "303130323930303030630333435"
    },
    {
        "Name": "Наименование товара 2",
        "Price": 3500,
        "Quantity": 2,
        "Amount": 7000,
        "Tax": "vat20"
    },
    {
        "Name": "Наименование товара 3",
        "Price": 550,
        "Quantity": 4,
        "Amount": 4200,
        "Tax": "vat10"
    }
]
}
}
"""END PAYMENT DATA"""

