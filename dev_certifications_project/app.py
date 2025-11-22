import os
from flask import Flask, render_template

app = Flask(__name__)

# Development Environment
os.environ['FLASK_DEBUG'] = 'True'
app.debug = os.environ.get('FLASK_DEBUG') == 'True'

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


if __name__ == '__main__':
    app.run()