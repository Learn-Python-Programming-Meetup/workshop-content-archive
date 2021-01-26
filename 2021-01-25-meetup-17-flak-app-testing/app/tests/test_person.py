
from app.main import create_app


def test_create_api():
    app = create_app()
    client = app.test_client()
    res = client.post('/person/', json={"name": "gandhi", "email": "g@y.com"})
    assert res.status_code == 202


def test_get_api():
    app = create_app()
    client = app.test_client()
    res = client.get('/person/')
    assert res.status_code == 200