from django.db import models
from userapp.models import User
from planapp.models import Plan
from datetime import timedelta

# Create your models here.
class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    order_id = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    used_credits = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.user.username} - {self.plan.name if self.plan else 'No plan'}"
    
    def save(self, *args, **kwargs):
        if not self.end_date and self.plan:
            # افتراض: مدة الباقة شهر واحد
            self.end_date = self.start_date + timedelta(days=30)
        super().save(*args, **kwargs)