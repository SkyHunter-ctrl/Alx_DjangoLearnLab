# Create
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="The Lemamas Empire", author="Nancy Nayianoi Ledama", publication_year=2025)
>>> book = Book.objects.get(id=1)
