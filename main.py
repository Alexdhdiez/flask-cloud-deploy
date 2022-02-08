from flask import Flask
from flask import jsonify
from handlers import create_app

app = Flask(__name__) # App has to be found in main for deployment
create_app(app)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8091, debug=True)
