import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Create sample data
author = Author.objects.create(name="J.K. Rowling")
b1 = Book.objects.create(title="Harry Potter 1", author=author)
b2 = Book.objects.create(title="Harry Potter 2", author=author)

library = Library.objects.create(name="Central Library")
library.books.add(b1, b2)

librarian = Librarian.objects.create(name="Alice", library=library)

# 2️⃣ Query all books by a specific author
books_by_author = Book.objects.filter(author=author)
print("Books by J.K. Rowling:")
for book in books_by_author:
    print(book.title)

# 3️⃣ List all books in a library
print("\nBooks in Central Library:")
for book in library.books.all():
    print(book.title)

# 4️⃣ Retrieve the librarian for a library
print("\nLibrarian for Central Library:", librarian.name)