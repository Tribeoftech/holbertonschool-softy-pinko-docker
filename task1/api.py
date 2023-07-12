from flask import flask

app = Flask(name)

@app.route('/')
def home():
    return 'Welcome to the Flask application!'

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if name == 'main':
    app.run(host='0.0.0.0', port=5252)
