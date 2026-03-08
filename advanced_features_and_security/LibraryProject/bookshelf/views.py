from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
from .models import Book
from django.utils.deprecation import MiddlewareMixin


# Secure book list view using Django ORM (prevents SQL injection)
def book_list(request):
    query = request.GET.get("q", "")

    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, "bookshelf/book_list.html", {
        "books": books,
        "query": query
    })


# Example form view with CSRF protection
def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Normally you would process the data here
            return render(request, "bookshelf/form_example.html", {
                "form": ExampleForm(),
                "success": True
            })
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})


class ContentSecurityPolicyMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response["Content-Security-Policy"] = "default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self'"
        return response


# Permission protected views
@permission_required('bookshelf.can_view', raise_exception=True)
def protected_book_list(request):
    return HttpResponse("Book list view")


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    return HttpResponse("Book create view")


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request):
    return HttpResponse("Book edit view")


@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request):
    return HttpResponse("Book delete view")