from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app.models.favorite import Favorite

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

@app.route("/authors/<int:id>")
def r_author_show(id):
    dictionary = {"id": id}
    return render_template("author_favorites.html", author_favorites = Author.get_author_with_favbooks(dictionary), books = Book.get_all_books())

@app.route("/authors/<int:id>/add-favorite", methods=["POST"])
def f_add_favorite(id):
    author_id = id
    book_id = request.form["book_id"]
    dictionary = {
        "author_id": author_id,
        "book_id": book_id
    }
    Favorite.add_favorite(dictionary)
    return redirect(f"/authors/{author_id}")

@app.route("/books/<int:id>")
def r_book_show(id):
    dictionary = {"id": id}
    return render_template("book_favorites.html", book_fans = Book.get_book_with_fans(dictionary), fans = Author.get_all_authors())

@app.route("/books/<int:id>/add-fan", methods=["POST"])
def f_add_fan(id):
    book_id = id
    author_id = request.form["author_id"]
    dictionary = {
        "author_id": author_id,
        "book_id": book_id
    }
    Favorite.add_favorite(dictionary)
    return redirect(f"/books/{book_id}")