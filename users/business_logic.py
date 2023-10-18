from datetime import datetime, timezone
from django.db.models import Avg, F, ExpressionWrapper, fields
from .models import CustomUser  # adjust the import based on your project structure

def calculate_average_time_since_joined():
    annotated_users = CustomUser.objects.annotate(
        time_since_joined=ExpressionWrapper(
            datetime.now(timezone.utc) - F('date_joined'),  # type: ignore
            output_field=fields.DurationField()
        )
    )
    # Calculate the average time delta
    average_time_since_joined = annotated_users.aggregate(
        avg_time=Avg('time_since_joined')
    )['avg_time']

    if average_time_since_joined:
        return average_time_since_joined
    else:
        return "No users to calculate."
