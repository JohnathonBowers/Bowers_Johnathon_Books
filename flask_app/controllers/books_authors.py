from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/')
def home():
    return redirect ('/authors')

@app.route('/authors')
def r_show_authors():
    return render_template('add_author.html', authors = Author.get_all_authors)