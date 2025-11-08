from abc import ABC, abstractmethod

class PaymentHandler(ABC):
    @abstractmethod
    def create_order(self, data):
        """Create payment order and return payment link"""
        pass