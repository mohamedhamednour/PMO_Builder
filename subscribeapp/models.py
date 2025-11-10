from django.db import models
from userapp.models import User
from planapp.models import Plan
from datetime import timedelta
from subscribeapp.validation import ValidationSubscription

# Create your models here.
class Subscription(models.Model  , ValidationSubscription):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='subscription')
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    order_id = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    total_credits = models.PositiveIntegerField(default=0)
    used_credits = models.PositiveIntegerField(default=0)
    used_projects = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.user.username} - {self.plan.name if self.plan else 'No plan'}"
    def save(self, *args, **kwargs):
        if not self.end_date and self.plan:

            self.end_date = self.start_date + timedelta(days=30)

        self.full_clean()
        super().save(*args, **kwargs)


class Stage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cost = models.PositiveIntegerField(default=20, help_text="Cost in credits per stage")

    def __str__(self):
        return f"{self.name} ({self.cost} credits)"