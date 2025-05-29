def send_alert(notification):
    """
    Sends an alert notification to the appropriate channel.
    
    Args:
        notification (str): The alert message to be sent.
    """
    # Implementation for sending the alert (e.g., via email, SMS, etc.)
    print(f"Alert sent: {notification}")

def process_alert_data(data):
    """
    Processes incoming alert data and prepares it for notification.
    
    Args:
        data (dict): The alert data to be processed.
    
    Returns:
        str: A formatted alert message.
    """
    # Example implementation for processing alert data
    alert_message = f"Alert: {data.get('type')} - {data.get('message')}"
    return alert_message

def handle_alert(data):
    """
    Handles an incoming alert by processing the data and sending a notification.
    
    Args:
        data (dict): The alert data to be handled.
    """
    formatted_message = process_alert_data(data)
    send_alert(formatted_message)