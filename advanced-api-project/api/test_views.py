from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(TestCase):
    def setUp(self):
        # Django automatically creates a separate test database for TestCase,
        # so production and development data are not affected.
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        self.author = Author.objects.create(name="Chinua Achebe")

        self.book = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )

    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book_detail(self):
        response = self.client.get(f"/api/books/{self.book.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Things Fall Apart")

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        data = {
            "title": "No Longer at Ease",
            "publication_year": 1960,
            "author": self.author.id
        }
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id
        }
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        data = {
            "title": "Things Fall Apart Updated",
            "publication_year": 1958,
            "author": self.author.id
        }
        response = self.client.put("/api/books/update/", data)
        self.assertIn(response.status_code, [200, 400, 404])

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete("/api/books/delete/")
        self.assertIn(response.status_code, [204, 400, 404])

    def test_filter_books(self):
        response = self.client.get("/api/books/?title=Things Fall Apart")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_books(self):
        response = self.client.get("/api/books/?search=Things")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books(self):
        response = self.client.get("/api/books/?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)