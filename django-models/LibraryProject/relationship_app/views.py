from django.shortcuts import render

# Function-based View to list books
from .models import Book
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', context={'books': books})
# Class-based View to show book details
from django.views.generic import DetailView 
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
# the hello_view function takes an HTTP request (request) as input and returns an HTTP response containing the string “Hello, World!”.
from django.http import HttpResponse
def hello_view(request):
    return HttpResponse("Hello, World!")


    
