from datetime import datetime, timedelta
from .models import Protocol  # adjust the import based on your project structure
from protocol_app.models import Protocol

def calculate_average_days_since_last_update():
    protocols = Protocol.objects.all()
    total_days = 0
    for protocol in protocols:
        delta = datetime.now() - protocol.last_updated.replace(tzinfo=None)
        total_days += delta.days

    if len(protocols) > 0:
        return total_days / len(protocols)
    else:
        return "No protocols to calculate."

def fetch_protocols_by_role(user_role):
    if user_role == 'admin':
        protocols = Protocol.objects.all()
    elif user_role == 'manager':
        protocols = Protocol.objects.filter(access_level__in=['manager', 'worker'])
    else:  # role is 'worker'
        protocols = Protocol.objects.filter(access_level='worker')

    # Format the protocols for GPT-3
    formatted_protocols = "\n".join([f"{protocol.title}: {protocol.description}" for protocol in protocols])
    return formatted_protocols
