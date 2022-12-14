
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

author1 = Author('Louise')
author2 = Author('Ben')
author3 = Author('Jack')

author_repo.save(author1)
author_repo.save(author2)
author_repo.save(author3)

book1 = Book('title1', author1, 'fiction')
book2 = Book('title2', author2, 'fiction')
book3 = Book('title3', author1, 'horror')

book_repo.save(book1)
book_repo.save(book2)
book_repo.save(book3)

x = book_repo.select_all()
for book in x:
    print(book.__dict__)
    print(book.author.__dict__)

