from django.contrib import admin
from .models import Subscription , Stage
# Register your models here.
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan','order_id' ,'start_date', 'end_date', 'is_active', 'used_credits')


@admin.register(Stage)  
class StageAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost') 


#     def get_queryset(self, request):
#         stages_data = [
#     {"name": "الاستراتيجية", "cost": 20},
#     {"name": "الحوكمه", "cost": 20},
#     {"name": "التشغيل", "cost": 20},
#     {"name": "الخدمات", "cost": 20},
#     {"name": "الفعالية", "cost": 20},
# ]
#         Stage.objects.bulk_create(Stage(name=stage_data['name'], cost=stage_data['cost']) for stage_data in stages_data)
#         return super().get_queryset(request).order_by('cost')