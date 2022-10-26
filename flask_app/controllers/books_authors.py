from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route("/")
def home():
    return redirect ("/authors")

@app.route("/authors")
def r_get_all_authors():
    return render_template("add_author.html", authors = Author.get_all_authors())

@app.route("/authors/add", methods=["POST"])
def f_save_author():
    Author.save_author(request.form)
    return redirect("/authors")

@app.route("/books")
def r_get_all_books():
    return render_template("add_book.html", books = Book.get_all_books())

@app.route("/books/add", methods=["POST"])
def f_save_book():
    Book.save_book(request.form)
    return redirect("/books")