from django.db import models

# Create your models here.


class TransactionPayment(models.Model) :
    payment_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
