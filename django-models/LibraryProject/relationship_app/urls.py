# Configure URL Patterns
from django.urls.py import path
from .views import list_books, LibraryDetailView, hello_view
from .import views
urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('about/', views.AboutView.as_view(), name='about'),
]
