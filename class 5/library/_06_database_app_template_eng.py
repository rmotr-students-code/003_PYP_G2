"""
Requirements:
 * A database created with some data about authors inside.
"""
import sqlite3
from flask import Flask, g, render_template

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')


@app.before_request
def before_request():
    g.db = connect_db()


@app.route('/')
def hello_world():
    cursor = g.db.execute('SELECT id, name FROM author;')
    authors = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    return render_template('authors_template_engine.html', authors=authors)
