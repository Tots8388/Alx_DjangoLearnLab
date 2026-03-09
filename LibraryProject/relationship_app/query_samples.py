import os
import sys
import django

# 1️⃣ Add the project root to sys.path
# This should be the folder containing manage.py
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# 2️⃣ Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

# 3️⃣ Setup Django
django.setup()

# 4️⃣ Import your models
from relationship_app.models import Author, Book, Library, Librarian

# Sample queries
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        print(f"Books by {author_name}: {[book.title for book in author.books.all()]}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f"Books in {library_name}: {[book.title for book in library.books.all()]}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        print(f"Librarian of {library_name}: {library.librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")

# Example usage
if __name__ == "__main__":
    books_by_author("J.K. Rowling")
    books_in_library("Central Library")
    librarian_for_library("Central Library")