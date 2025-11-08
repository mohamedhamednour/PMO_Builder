from django.contrib import admin
from .models import Plan
# Register your models here.
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_month', 'credits_per_month', 'project_limit', 'features')