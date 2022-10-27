from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
from flask_app.models import author

class Favorite:
    def __init__(self, db_data):
        self.author_id = db_data["author_id"]
        self.book_id = db_data["book_id"]

    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL("books_authors_schema").query_db(query, data)