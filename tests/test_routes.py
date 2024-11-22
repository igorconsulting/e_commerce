import pytest
from app.models import db, User

@pytest.fixture
def client():
    from main import app
    # Dependency Injection: Test database configuration injected into the app.
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Factory Pattern: Creates test database schema.
        yield client

# Test for user registration
def test_register(client):
    response = client.post('/register', json={'username': 'testuser', 'password': '1234'})
    assert response.status_code == 201
    assert b'User registered successfully' in response.data
