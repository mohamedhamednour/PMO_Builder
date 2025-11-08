from rest_framework import  viewsets , mixins
from rest_framework import status
from rest_framework.response import Response
from django.db import transaction


from .serializers import SubscriptionSerializer
from .models import Subscription
from shared.factorypayment import PaymentFactory
from shared.data_validation import  DataCreatePayment  , BillingData
class SubscribeViewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ## start transaction
        with transaction.atomic():  
            serializer.save()
            subscription = serializer.instance
            plan = subscription.plan
            ## get payment data

            data = DataCreatePayment(
                amount=int(plan.price_per_month * 100),
                payment_methods=[5075202],
                billing_data=BillingData(
                    first_name=request.user.first_name or "NA",
                    last_name=request.user.last_name or "NA",
                    email=request.user.email or "test@example.com",
                    phone_number="01000000000",
                ),
            )
            ## create order
            handler = PaymentFactory.get_handler('paymob')
            handler.create_order(data.dict())  
            ##edit order id
            order_id = handler.order["payment_keys"][0]["order_id"]
            subscription.order_id = order_id
            subscription.save()
            ## get payment link 
            payment_link = handler.get_payment_link() 

            return Response(
                {"payment_link": payment_link}, 
                status=status.HTTP_201_CREATED
            )
