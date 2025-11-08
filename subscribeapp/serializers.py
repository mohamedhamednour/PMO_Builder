from rest_framework import serializers
from .models import Subscription
from datetime import datetime

class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Subscription
        fields = ('user', 'plan')


    def validate(self, data):
        user = self.context['request'].user
        now = datetime.now()

        active_subscription = (
            Subscription.objects.filter(user=user, is_active=True).first()
        )

        if active_subscription and active_subscription.end_date >= now:
            raise serializers.ValidationError(
                "You already have an active subscription. Please wait until it ends."
            )

        return data
