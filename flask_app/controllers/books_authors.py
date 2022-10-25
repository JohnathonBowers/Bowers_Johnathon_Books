from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/')
def home():
    return redirect ('/authors')