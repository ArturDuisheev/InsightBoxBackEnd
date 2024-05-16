import requests

a = requests.get('http://127.0.0.1:8000/',)
print("fd", a.headers.get('Cross-Origin-Opener-Policy'))