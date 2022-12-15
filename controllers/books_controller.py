from flask import Flask ,Blueprint, render_template, redirect, request
import repositories.book_repository as book_repo
import repositories.author_repository as author_repo
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def index():
    books = book_repo.select_all()
    return render_template("books/index.html", books=books)

@books_blueprint.route("/books/delete/<id>", methods = ['POST'])
def destroy(id):
    book_repo.delete(id)
    return redirect("/books")

@books_blueprint.route("/books/new")
def new():
    author_list = author_repo.select_all()
    return render_template("books/new.html", all_authors = author_list)

@books_blueprint.route("/books", methods=['POST'])
def create():
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    author = author_repo.select(author_id)
    book = Book(title, author, genre)
    book_repo.save(book)
    return redirect("/books")

@books_blueprint.route("/books/edit/<id>")
def edit(id):
    book = book_repo.select(id)
    authors = author_repo.select_all()
    return render_template("books/edit.html", book = book, all_authors = authors)

@books_blueprint.route("/books/<id>", methods=['POST'])
def update(id):
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    author = author_repo.select(author_id)
    book = Book(title, author, genre, id)
    book_repo.update(book)
    return redirect("/books")

