from datetime import timedelta, datetime, timezone
from django.core.exceptions import ValidationError

class ValidationSubscription:

    def validate_end_date(self):
        now = datetime.now(timezone.utc)
        if self.end_date and now > self.end_date:
            self.is_active = False
            
            raise ValidationError("expired subscription")

    def clean(self):
        self.validate_end_date()
        super().clean()


    