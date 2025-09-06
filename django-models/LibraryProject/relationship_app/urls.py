# Configure URL Patterns
from django.urls.py import path
from .import views
urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('about/', views.AboutView.as_view(), name='about'),
]
