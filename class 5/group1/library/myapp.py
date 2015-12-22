import os

from flask import Flask, render_template, g, request
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')

@app.before_request
def before_request():
    g.db = connect_db()

@app.route('/')
def render_home():
    title = 'Home'
    return render_template('home.html',title=title)

@app.route('/all-authors')
def render_author_list():
    cursor1 = g.db.execute('SELECT a.id, a.name, c.name FROM author a INNER JOIN country c ON a.country_id = c.id;')
    authors = [dict(id=row[0], name=row[1], country=row[2]) for row in cursor1.fetchall()]
    title = 'All Authors'
    return render_template('author-list.html', authors=authors,title=title)
    
@app.route('/author/<int:author_id>')
def render_author_books(author_id):
    cursor2 = g.db.execute('SELECT name from author where id = ?', [author_id])
    author = cursor2.fetchone()[0]

    cursor3 = g.db.execute('SELECT b.id, b.title FROM book b WHERE b.author_id = ?', [author_id])
    books = [dict(id=row[0], title = row[1]) for row in cursor3.fetchall()]
    title = 'Books by ' + str(author)
    return render_template('books-by-author.html', author=author, books=books,title=title)


@app.route('/book/<int:book_id>')
def render_book_info(book_id):
    cursor = g.db.execute('SELECT title, isbn FROM book WHERE id = ?', [book_id])
    book_list = cursor.fetchone()
    book = { 'title': book_list[0], 'isbn': book_list[1] }
    title = book['title']
    return render_template('book.html', book=book,title=title)
    

@app.route('/addbook', methods = ['GET','POST'])
def render_add_book():
    title = 'Add Books'
    cursor1 = g.db.execute('SELECT id, name FROM author')
    authors = [dict(id=row[0], name=row[1]) for row in cursor1.fetchall()]
    if request.method == 'GET':
        return render_template('simple_form.html',title=title,authors=authors)
    elif request.method == 'POST':
        if request.form['author_new'] != '':
            cursor = g.db.execute('INSERT into author (name) VALUES (?)', [request.form['author_new']])
            g.db.commit()
            author_id = cursor.lastrowid
            cursor = g.db.execute('INSERT into book (title,isbn,author_id) VALUES (?,?,?)', [request.form['title'],request.form['isbn'],author_id])
            g.db.commit()
            return render_template('simple_form.html',title=title,authors=authors)
        elif request.form['author_new'] == '' and request.form['author'] != '':
            cursor = g.db.execute('INSERT into book (title,isbn,author_id) VALUES (?,?,?)', [request.form['title'],request.form['isbn'],request.form['author']])
            g.db.commit()
            return render_template('simple_form.html',title=title,authors=authors)
        







