#function-based view to list all books
from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
# Class-based View to show book details 
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
# the hello_view function takes an HTTP request (request) as input and returns an HTTP response containing the string “Hello, World!”.
from django.http import HttpResponse
def hello_view(request):
    return HttpResponse("Hello, World!")
#


    
