from django.shortcuts import render
from .models import Book
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', context={'books': books})
# Class-based View to show book details 
from django.views.generic.detail import DetailView
from .models import Library
class BookDetailView(DetailView):
    model = Library
    library = 'relationship_app/library_detail.html'
    context_object_name = 'book'
# the hello_view function takes an HTTP request (request) as input and returns an HTTP response containing the string “Hello, World!”.
from django.http import HttpResponse
def hello_view(request):
    return HttpResponse("Hello, World!")
#


    
