from bookshelf.models import Book
Book.objects.get(title="Nineteen Eighty-Four").delete()
Book.objects.all()