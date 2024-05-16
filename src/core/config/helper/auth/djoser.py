DJOSER = {
    'USER_CREATE_PASSWORD_RETYPE': False,
    'SEND_ACTIVATION_EMAIL': True,
    'SET_PASSWORD_RETYPE': False,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'TOKEN_MODEL': None,
    'ACTIVATION_URL': 'auth/verify/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_URL': 'api/v1/djoser/auth/password/reset/confirm/{uid}/{token}',
}