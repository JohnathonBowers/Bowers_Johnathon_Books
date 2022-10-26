from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__ (self, db_data):
        self.id = db_data["id"]
        self.title = db_data["title"]
        self.num_of_pages = db_data["num_of_pages"]
        self.created_at = db_data["created_at"]
        self.updated_at = db_data["updated_at"]
        self.author_fans = []

    @classmethod
    def save_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        return connectToMySQL("books_authors_schema").query_db(query, data)
    
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books ORDER BY title ASC;"
        results = connectToMySQL("books_authors_schema").query_db(query)
        book_objects = []
        for book in results:
            book_objects.append(cls(book))
        return book_objects
    
    @classmethod
    def get_book_with_fans(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL("books_authors_schema").query_db(query, data)
        book = cls( results[0] )
        for row_from_db in results:
            author_fan_data = {
                "id":row_from_db["authors.id"],
                "name":row_from_db["name"],
                "created_at":row_from_db["authors.created_at"],
                "updated_at":row_from_db["authors.updated_at"]
            }
            book.author_fans.append(author.Author(author_fan_data))