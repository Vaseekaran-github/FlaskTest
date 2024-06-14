import pytest
from app import create_app, db
from app.models import TestWord

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    with app.app_context():
        db.create_all()
        db.session.add(TestWord(word="Test"))
        db.session.commit()

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_test_word(client):
    response = client.get('/api/test-word')
    assert response.status_code == 200
    assert response.json == {"word": "Test"}

def test_update_word(client):
    response = client.get('/admin/update-word', json={"word": "UpdatedTest"})
    assert response.status_code == 200
    assert response.json == {"message": "Word updated successfully"}

    response = client.get('/api/test-word')
    assert response.status_code == 200
    assert response.json == {"word": "UpdatedTest"}
