import os

class Config:
    """Configuration settings for the bot."""
    
    API_KEY = os.getenv("API_KEY", "your_default_api_key")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")
    DEBUG = os.getenv("DEBUG", "False") == "True"