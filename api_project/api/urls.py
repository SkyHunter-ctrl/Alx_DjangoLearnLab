from django.urls import path
from .views import BookList
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]

# Set Up a Router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='bool_all' )

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # optional
    path('', include(router.urls)),  # this includes /books_all/

]