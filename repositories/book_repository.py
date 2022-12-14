from db.run_sql import run_sql
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repo

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repo.select(row['author_id'])
        book = Book(row['title'], author, row['genre'], row['id'])
        books.append(book)
    return books

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def save(book):
    sql = "INSERT INTO books (title, author_id , genre) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id 
    return book
