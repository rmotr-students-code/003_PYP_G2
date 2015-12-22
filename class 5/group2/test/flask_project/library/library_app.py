import os

from flask import Flask, g, render_template
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')

@app.before_request
def before_request():
    g.db = connect_db()

@app.route('/')
def hello_world():
    library_name = 'Epic'
    return render_template('index.html', library_name=library_name)

@app.route('/add')
def add():
    return render_template('add.html')
    
@app.route('/remove')
def remove():
    return render_template('remove.html')
    
   
@app.route('/edit')
def edit():
    return render_template('edit.html')
    
@app.route('/viewlibrary')
def viewlibrary():
    return render_template('view.html')
    
    
@app.route('/book/<int:book_id>')
def view_book(book_id):
    cursor = g.db.execute('SELECT title, isbn FROM book WHERE id = ?', book_id)
    book_list = cursor.fetchone()
    book = { 'title': book_list[0], 'isbn': book_list[1] }
    return render_template('book.html', book=book)
    
'''
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
'''