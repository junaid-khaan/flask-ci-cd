import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    json_data = response.get_json()
    assert json_data['message'] == "Hello, World!"
