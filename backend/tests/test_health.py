from fastapi.testclient import TestClient
from backend.app.main import app

def test_health_check(client):
    """Test the health check endpoint returns correct response"""
    response = client.get("/health")
    
    # Test status code
    assert response.status_code == 200
    
    # Test response content type
    assert response.headers["content-type"] == "application/json"
    
    # Test exact response body
    assert response.json() == {
        "status": "healthy",
        "service": "hazard-alert-bot",
        "version": "1.0.0"
    }