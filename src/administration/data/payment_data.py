
"""BEGIN PAYMENT DATA"""
api_url: str = 'https://securepay.tinkoff.ru/v2/' #TODO: поместить в .env

terminal_key = '1693924570978DEMO'

terminal_password = 'r648vd0pmclgj2kd'

payment_data: dict = {
    'TerminalKey': terminal_key,
    'Password': terminal_password,
    'Amount': 13,
    'OrderId': '123',
    'Description': 'Payment request test',
    'Token': None,
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

