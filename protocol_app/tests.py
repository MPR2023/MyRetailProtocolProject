from django.test import TestCase
from datetime import datetime, timedelta
from protocol_app.models import Protocol
from protocol_app.business_logic import calculate_average_days_since_last_update, fetch_protocols_by_role  # Adjust the import based on your project structure

class BusinessLogicTestCase(TestCase):

    def test_average_days_no_protocols(self):
        result = calculate_average_days_since_last_update()
        self.assertEqual(result, "No protocols to calculate.")

    def test_average_days_same_last_updated(self):
        Protocol.objects.create(title="Test1", last_updated=datetime.now())
        Protocol.objects.create(title="Test2", last_updated=datetime.now())
        result = calculate_average_days_since_last_update()
        self.assertEqual(result, 0)

    def test_fetch_protocols_invalid_role(self):
        result = fetch_protocols_by_role('invalid_role')
        self.assertEqual(result, "")

    def test_fetch_protocols_no_protocols_for_role(self):
        # Create a protocol with access_level 'admin'
        Protocol.objects.create(title="Admin Protocol", access_level='admin')
        # Try to fetch protocols for 'worker', should return empty
        result = fetch_protocols_by_role('worker')
        self.assertEqual(result, "")
