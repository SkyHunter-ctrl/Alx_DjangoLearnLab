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
router.register(r'books_all', BookViewSet, basename= 'book_all')

urlpatterns = [
    path('api/', include(router.urls)), # This includes all routes registered with the router
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),
]