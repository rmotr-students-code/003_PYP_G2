from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship('Country', backref=db.backref('authors', lazy='dynamic'))

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __repr__(self):
        return '<Author %r>' % self.name


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Country %r>' % self.name
        

@app.route('/')
def hello_world():
    return 'Welcome to our Library!'
