from flask import Flask ,Blueprint, render_template, redirect
import repositories.book_repository as book_repo


books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def index():
    books = book_repo.select_all()
    return render_template("books/index.html", books=books)

@books_blueprint.route("/books/<id>", methods = ['POST'])
def destroy(id):
    book_repo.delete(id)
    return redirect("/books")