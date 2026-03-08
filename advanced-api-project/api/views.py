from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# List all books / create a new book
# Unauthenticated users can read, authenticated users can create.
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Retrieve, update, or delete a single book by ID
# Unauthenticated users can read, authenticated users can modify only if authenticated.
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]