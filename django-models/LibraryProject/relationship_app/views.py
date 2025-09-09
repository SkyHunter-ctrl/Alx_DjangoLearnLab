# Task 1 Django views and urls configs
# implementing function-based view
from django.shortcuts import render
from .models import Book
def list_books(request):
    books = Book.objects.all() # fetch all book isntances
    context = {"list_books": books} # creates context dictionanry with bok list
    return render(request, 'relationship_app/list_books.html' context)

# implementing Class-based view
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

