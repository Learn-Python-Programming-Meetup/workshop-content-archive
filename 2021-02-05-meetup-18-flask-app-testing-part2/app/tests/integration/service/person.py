import pytest
import os

from flask_sqlalchemy import SQLAlchemy

from app.main import create_app
from app.service.person import PersonService


@pytest.fixture
def db_connection():
    DB_NAME = "integration_test_db"
    app = create_app(DB_NAME)
    db = SQLAlchemy(app)
    yield db
    db_path = os.path.dirname(os.path.abspath(__file__)) + '/../../../'
    os.remove(db_path + DB_NAME + '.sqlite')


@pytest.fixture
def user1():
    return {"id": 1,
            "name": "gandhi",
            "email": "g@y.com"}


@pytest.fixture
def user2():
    return {"id": 2,
            "name": "nishant",
            "email": "n@y.com"}


def test_create(user1, db_connection):
    person = PersonService(db_connection)
    assert person.create(name=user1['name'], primary_email=user1['email']) is True


def test_retrieve(user1, user2, db_connection):
    person = PersonService(db_connection)

    person.create(name=user1['name'], primary_email=user1['email'])
    person.create(name=user2['name'], primary_email=user2['email'])

    data = person.retrieve()
    assert data[0].name == user1['name']
    assert data[0].primary_email == user1['email']

    assert data[1].name == user2['name']
    assert data[1].primary_email == user2['email']


def test_retrieve_one(user1, user2, db_connection):
    person = PersonService(db_connection)

    person.create(name=user1['name'], primary_email=user1['email'])
    person.create(name=user2['name'], primary_email=user2['email'])

    data = person.retrieve_one(id=2)
    assert data.name == user2['name']
    assert data.primary_email == user2['email']