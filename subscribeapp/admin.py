from django.contrib import admin
from .models import Subscription
# Register your models here.
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan','order_id' ,'start_date', 'end_date', 'is_active', 'used_credits')