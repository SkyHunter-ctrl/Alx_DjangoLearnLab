# Task 1 Django views and urls configs
# implementing function-based view
from django.shortcuts import render
from .models import Book
def book_list(request):
    books = Book.objects.all() # fetch all book isntances
    context = {"book_list": books} # creates context dictionanry with bok list
    return render(request, 'relationship_app/book_list.html' context)

# implementing Class-based view
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

