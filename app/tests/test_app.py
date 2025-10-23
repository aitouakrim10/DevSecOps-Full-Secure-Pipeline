from app import app
import pytest

def test_home_page():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Timezone Information" in response.data

def test_health_check():
    with app.test_client() as client:
        response = client.get('/healthz')
        assert response.status_code == 200
        assert b"OK" in response.data
