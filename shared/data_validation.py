from dataclasses import dataclass, asdict
from typing import List

PAYMOB_INTEGRATION_ID_CAPTURE = 5075202 

@dataclass
class BillingData:
    first_name: str
    last_name: str
    phone_number: str
    email: str
    apartment: str = "NA"
    floor: str = "NA"
    street: str = "NA"
    building: str = "NA"
    shipping_method: str = "NA"
    postal_code: str = "NA"
    city: str = "Cairo"
    country: str = "EG"
    state: str = "NA"


@dataclass
class DataCreatePayment:
    amount: int
    billing_data: BillingData
    payment_methods: List[int] 
    currency: str =  "EGP"

    def dict(self):
        return asdict(self)
