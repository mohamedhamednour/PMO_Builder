from django.db import transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from userapp.models import User
from .models import Subscription, Plan


@api_view(['POST'])
@permission_classes([AllowAny]) 
def paymob_callback(request):
    """
    This endpoint handles Paymob's transaction processed callback.
    """
    try:
        data = request.data  

        success = data.get("success")
        if not success or str(success).lower() != "true":
            return Response({"error": "Payment not successful"}, status=400)

        with transaction.atomic():
            # أوقف أي اشتراك نشط سابق
            old_subscription = Subscription.objects.filter(is_active=True , email=data.get('email')).first()
            remaining_credits = old_subscription.used_credits if old_subscription else 0

            if old_subscription:
                old_subscription.is_active = False
                old_subscription.save()

            # 4️⃣ أنشئ الاشتراك الجديد
            new_subscription = Subscription.objects.create(
                order_id=data.get("order_id"),
            )
            new_subscription.total_credits += remaining_credits
            new_subscription.is_active = True
            new_subscription.save()

        return Response({
            "status": "success",
            "subscription_id": new_subscription.id
        })

    except Exception as e:
        return Response({"error": str(e)}, status=500)
