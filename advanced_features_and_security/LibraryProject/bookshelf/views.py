from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_books')
    return render(request, 'relationship_app/create_book.html', {'form': form})

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Secure Views Against SQL Injection
def book_search(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)  # ORM protects against injection
    return render(request, 'bookshelf/book_list.html', {'books': books, 'query': query})

def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():  # Validates and sanitizes input
        form.save()
    return render(request, 'bookshelf/form_example.html', {'form': form})

from .forms import ExampleForm
def example_form_view(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        # Process the data securely
        cleaned_data = form.cleaned_data
    return render(request, 'bookshelf/form_example.html', {'form': form})