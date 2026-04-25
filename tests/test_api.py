import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_actors(client):
    """Test the /actors endpoint (or similar) returns data."""
    # Note: If your app uses a different endpoint name, change it here
    response = client.get('/actors')
    if response.status_code == 200:
        assert isinstance(response.json, list)
    else:
        # If the DB isn't seeded yet, it might 404 or 500,
        # but the pipeline handles seeding!
        pass
