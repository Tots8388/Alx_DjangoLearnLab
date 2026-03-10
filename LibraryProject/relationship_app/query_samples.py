import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books = Book.objects.filter(author=author)

print("Books by author:")
for book in books:
    print(book.title)


# List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()

print("\nBooks in library:")
for book in books_in_library:
    print(book.title)


# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)

print("\nLibrarian:", librarian.name)