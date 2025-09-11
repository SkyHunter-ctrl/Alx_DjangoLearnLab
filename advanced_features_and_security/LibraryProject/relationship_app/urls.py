# task 1 config url patterns
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

#Task 2: configure urls for user authothication
from django.urls import path
from .views import user_login, user_logout, register

urlpatterns += [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Function-based registration view
    path('register/', views.register, name='register'),

    # Class-based login view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Class-based logout view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
#Task 3: config 
from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns += [
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
]

# task 4;
from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns += [
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]

