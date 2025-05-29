import unittest
from src.handlers.alerts import handle_alert

class TestAlertHandlers(unittest.TestCase):

    def test_handle_alert(self):
        # Example alert data
        alert_data = {
            'type': 'warning',
            'message': 'This is a test alert.'
        }
        result = handle_alert(alert_data)
        self.assertTrue(result)  # Assuming handle_alert returns True on success

if __name__ == '__main__':
    unittest.main()