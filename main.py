from flask import Flask
from flask import jsonify

def create_app():
    my_app = Flask(__name__)
    
    @my_app.route('/')
    def hello():
        """Return a friendly HTTP greeting."""
        print("I am inside hello world")
        return 'Hello World! Trying continuous deployment (CD)'
    
    @my_app.route('/echo/<name>')
    def echo(name):
        print(f"This was placed in the url: new-{name}")
        val = {"new-name": name}
        return jsonify(val)
    
    return my_app
    
if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=8091, debug=True)
