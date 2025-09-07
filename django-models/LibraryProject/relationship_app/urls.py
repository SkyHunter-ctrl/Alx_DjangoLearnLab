# Configure URL Patterns
from django.urls.py import path
from .views import list_books, LibraryDetailView, hello_view
from .import views
urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('about/', views.AboutView.as_view(), name='about'),
]
# accounts path which contains the login, logout, password change etc routes except the signup and profile routes
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]