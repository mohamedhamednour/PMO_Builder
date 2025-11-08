from django.db import models

# Create your models here.
from django.db import models
from .conf import PLAN_CHOICES
class Plan(models.Model):


    name = models.CharField(max_length=50, choices=PLAN_CHOICES, unique=True)
    price_per_month = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    credits_per_month = models.PositiveIntegerField()
    project_limit = models.CharField(max_length=50)
    features = models.TextField()

    class Meta:
        verbose_name = "Subscription Plan"
        verbose_name_plural = "Subscription Plans"
        ordering = ["price_per_month"]

    def __str__(self):
        return f"{self.name} - ${self.price_per_month}"
