from .abstractpayment import PaymentHandler
from shared.handlerpaymob import HandlerPaymob
class PaymentFactory:
    @staticmethod
    def get_handler(method: str) -> PaymentHandler:
        if method == "paymob":
            return HandlerPaymob()
        else:
            raise ValueError(f"Payment method {method} not supported")