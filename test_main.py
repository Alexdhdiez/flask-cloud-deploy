from main import create_app
from flask import jsonify

def test_hello():
    app = create_app()
    client = app.test_client()
    url = "/"
    response = client.get(url)
    assert b"Hello World" in response.get_data() 
    assert response.status_code == 200

def test_echo():
    app = create_app()
    client = app.test_client()
    url = "/echo/foo"
    response = client.get(url)
    assert response.json == {"new-name": "foo"}
    assert response.status_code == 200