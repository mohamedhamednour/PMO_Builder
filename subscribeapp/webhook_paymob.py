# from django.db import transaction

# def paymob_callback(request):
#     # 1️⃣ استخرج بيانات الدفع من CallBack
#     user_id = request.POST.get("user_id")
#     plan_id = request.POST.get("plan_id")
#     # التأكد من الدفع ناجح
#     payment_status = request.POST.get("success")  # حسب Paymob
#     if payment_status != "true":
#         return Response({"error": "Payment failed"}, status=400)

#     user = User.objects.get(id=user_id)
#     plan = Plan.objects.get(id=plan_id)

#     with transaction.atomic():
#         # 2️⃣ جلب الباقة القديمة النشطة إن وجدت
#         old_subscription = Subscription.objects.filter(user=user, is_active=True).first()

#         if old_subscription:
#             remaining_credits = old_subscription.used_credits
#             old_subscription.is_active = False
#             old_subscription.save()
#         else:
#             remaining_credits = 0

#         # 3️⃣ إنشاء الباقة الجديدة
#         new_subscription = Subscription.objects.create(
#             user=user,
#             plan=plan,
#             used_credits=remaining_credits,
#             is_active=True
#         )

#     return Response({"status": "success", "subscription_id": new_subscription.id})
