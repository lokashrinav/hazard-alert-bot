import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

@pytest.fixture
def client():
    """Test client fixture"""
    return TestClient(app)  # Pass app as a positional argument, not keyword