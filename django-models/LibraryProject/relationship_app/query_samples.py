from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="Chinua Achebe")
books_by_author = Book.objects.filter(author=author)
print("Books by specific author:")
for book in books_by_author:
    print(book.title)

# List all books in a library
library = Library.objects.get(name="City Library")
books_in_library = library.books.all()
print("\nBooks in library:")
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("\nLibrarian for library:")
print(librarian.name)