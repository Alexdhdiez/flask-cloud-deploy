from flask import Flask
from flask import jsonify

def create_app():
    global app 
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        """Return a friendly HTTP greeting."""
        print("I am inside hello world")
        return 'Hello World! Trying continuous deployment (CD)'
    
    @app.route('/echo/<name>')
    def echo(name):
        print(f"This was placed in the url: new-{name}")
        val = {"new-name": name}
        return jsonify(val)
    
    return app
    
if __name__ == '__main__':
    my_app = create_app()
    my_app.run(host='127.0.0.1', port=8091, debug=True)
