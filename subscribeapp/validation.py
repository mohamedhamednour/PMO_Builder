from datetime import timedelta, datetime, timezone
from django.core.exceptions import ValidationError

class ValidationSubscription:

    def validate_end_date(self):
        now = datetime.now(timezone.utc)
        if self.end_date and now > self.end_date:
            self.is_active = False
            
            raise ValidationError("expired subscription")
        
    def start_data_not_greater_than_end_date(self):
        if self.start_date > self.end_date:
            raise ValidationError("start date must be less than end date")
        

    def validate(self):
        self.validate_end_date()
        self.start_data_not_greater_than_end_date()

    def clean(self):
        self.validate()
        super().clean()


    