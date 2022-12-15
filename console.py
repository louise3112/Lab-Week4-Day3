
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

author_1 = Author("Jodi Piccoult")
author_2 = Author("C S Lewis")

author_repo.save(author_1)
author_repo.save(author_2)

book_1 = Book("The Pact", author_1, "Adult Fiction")
book_2 = Book("The Magician's Nephew", author_2, "Children's Fiction")
book_3 = Book("My Sister's Keeper", author_1, "Adult Fiction")

book_repo.save(book_1)
book_repo.save(book_2)
book_repo.save(book_3)

all_books = book_repo.select_all()
for book in all_books:
    print(book.__dict__)
    print(book.author.__dict__)

