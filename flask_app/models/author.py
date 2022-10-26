from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self, data):
        self.id = db_data["id"]
        self.name = db_data["name"]
        self.created_at = db_data["created_at"]
        self.updated_at = db_data["updated_at"]
        self.favorite_books = []
    
    @classmethod
    def save_author(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return connectToMySQL("books_authors_schema").query_db(query, data)
    
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors ORDER BY name ASC;"
        results = connectToMySQL("books_authors_schema").query_db(query)
        author_objects:list[object] = []
        for author in results:
            author_objects.append(cls(author))
        return author_objects

    @classmethod
    def get_author_with_favbooks(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL("books_authors_schema").query_db(query, data)
        author = cls( results[0] )
        for row_from_db in results:
            favorite_data = {
                "id":row_from_db["favorites.id"],
                "title":row_from_db["title"],
                "num_of_pages":row_from_db["num_of_pages"],
                "created_at":row_from_db["favorites.created_at"],
                "updated_at":row_from_db["favorites.updated_at"]
            }
            author.favorite_books.append(book.Book(favorite_data))
