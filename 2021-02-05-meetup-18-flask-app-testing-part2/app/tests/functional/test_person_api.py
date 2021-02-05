import pytest
import os
from app.main import create_app
import requests


@pytest.fixture
def user():
    return {"id": 1,
            "name": "gandhi",
            "email": "g@y.com"}


@pytest.fixture(scope='module')
def clean_up():
    yield
    db_path = os.path.dirname(os.path.abspath(__file__)) + '/../../'
    os.remove(db_path + 'db' + '.sqlite')
    create_app()


def test_create_api(user, clean_up):
    res = requests.post('http://localhost:7000/person/', json=user)
    assert res.status_code == 202


def test_get_api(user, clean_up):
    requests.post('http://localhost:7000/person/', json=user)
    res = requests.get('http://localhost:7000/person/')
    assert res.status_code == 200
    assert res.json()
    assert res.json()[0]['id'] == user['id']
    assert res.json()[0]['name'] == user['name']
    assert res.json()[0]['primary email'] == user['email']
