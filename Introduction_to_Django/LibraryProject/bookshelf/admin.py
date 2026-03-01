from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns visible in the admin list page
    list_display = ("title", "author", "publication_year")

    # Right-side filters in admin
    list_filter = ("author", "publication_year")

    # Search box fields
    search_fields = ("title", "author")