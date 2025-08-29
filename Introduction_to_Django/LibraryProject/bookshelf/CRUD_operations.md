#Markdown

# Create
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="The Lemamas Empire", author="Nancy Nayianoi Ledama", publication_year=2025)
>>> book = Book.objects.get(id=1)

# Retrive
>>> book = Book.objects.get(id=1)
>>> book.title
'The Lemamas Empire'
>>> book.author
'Nancy Nayianoi Ledama'
>>> book.publication_year
2025

# Update
>>> book = Book.objects.get(id=1)
>>> book.title = "Wood Empire"
>>> book.save
<bound method Model.save of <Book: Wood Empire by Nancy Nayianoi Ledama (2025)>>

# Delete
>>> book = Book.objects.get(id=1)
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
