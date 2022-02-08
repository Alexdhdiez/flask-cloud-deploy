from main import create_app
from flask import jsonify, Flask
from handlers import create_app

def test_hello():
    app = Flask(__name__)
    create_app(app)

    client = app.test_client()
    url = "/"
    response = client.get(url)
    assert b"Hello World" in response.get_data() 
    assert response.status_code == 200

def test_echo():
    app = Flask(__name__)
    create_app(app)
    
    client = app.test_client()
    url = "/echo/foo"
    response = client.get(url)
    assert response.json == {"new-name": "foo"}
    assert response.status_code == 200