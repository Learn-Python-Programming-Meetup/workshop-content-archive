
import pytest
import mock
from app.main import create_app
from app.model.person import Person


@pytest.fixture
def user():
    return {"name": "gandhi", "email": "g@y.com"}


def test_post_api(user):
    app = create_app()
    with app.test_client() as c:
        rv = c.post('/person/', json=user)
        assert rv.status_code == 202


def test_post_api_no_payload(user):
    app = create_app()
    with app.test_client() as c:
        rv = c.post('/person/', json={})
        assert rv.status_code == 422


def test_post_api_in_valid_payload(user):
    app = create_app()
    with app.test_client() as c:
        rv = c.post('/person/', json={'xyz': 123})
        assert rv.status_code == 422


def test_get_all_api():
    app = create_app()
    with app.test_client() as c:
        rv = c.get('/person/')
        assert rv.status_code == 200


@mock.patch('app.service.person.PersonService')
def test_get_one_api(mock_ps):
    app = create_app()
    mock_ps.return_value.retrieve_one.return_value = Person(name='wrong', primary_email='ncwk')
    with app.test_client() as c:
        rv = c.get('/person/123')
        assert rv.status_code == 200

