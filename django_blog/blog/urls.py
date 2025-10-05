from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)
from .views import search_posts, tagged_posts

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),         # ✅ Required
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # ✅ Required
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # ✅ Required
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-add'),     # ✅ Required
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),     # ✅ Required
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),     # ✅ Required
    path('search/', search_posts, name='search-posts'),
    path('tags/<str:tag_name>/', tagged_posts, name='tagged-posts'),
    


]



# 
