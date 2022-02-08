from flask import jsonify

def create_app(my_app):
    
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
    
