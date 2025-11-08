import requests
from .factorypayment import PaymentHandler

from decouple import config

PAYMOB_SECRET_KEY = config("PAYMOB_SECRET_KEY")
PAYMOB_PUBLIC_KEY = config("PAYMOB_PUBLIC_KEY")
PAYMOB_INTEGRATION_ID_CAPTURE = config("PAYMOB_INTEGRATION_ID_CAPTURE")
PAYMOB_BASE_URL = config("PAYMOB_BASE_URL")
PAYMENT_URL = f"https://accept.paymob.com/unifiedcheckout/?publicKey={PAYMOB_PUBLIC_KEY}&clientSecret="

class HandlerPaymob(PaymentHandler):

    def __init__(self):
        self.order = None

    def create_order(self , payload):
        url = f"{PAYMOB_BASE_URL}/intention"
        headers = {"Authorization": f"Token {PAYMOB_SECRET_KEY}"}
        response = requests.post(url, json=payload, headers=headers)
        print(response.json())
        self.order = response.json()
        return self.order

    def get_payment_link(self):
        """يرجع رابط الدفع النهائي"""
        if not self.order:
            raise Exception("You must create an order first!")
        client_secret = self.order.get("client_secret")
        return f"iframe src='{PAYMENT_URL}{client_secret}'></iframe>"


