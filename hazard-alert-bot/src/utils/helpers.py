def format_data(data):
    """Format data for output."""
    return str(data)

def log_message(message):
    """Log a message to the console."""
    print(f"[LOG] {message}")

def validate_input(input_data):
    """Validate input data."""
    if not input_data:
        raise ValueError("Input data cannot be empty.")
    return True