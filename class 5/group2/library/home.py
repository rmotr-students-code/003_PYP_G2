import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html') #add any passed variables as subsequent parameters.
