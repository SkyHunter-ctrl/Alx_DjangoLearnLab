from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book
class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass123')
        self.author = Author.objects.create(name='Chinua Achebe')
        self.book = Book.objects.create(
            title='Things Fall Apart',
            publication_year=1958,
            author=self.author
        )
        self.token_url = reverse('book-create')
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Things Fall Apart', str(response.data))

    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'No Longer at Ease',
            'publication_year': 1960,
            'author': self.author.id
        }
        response = self.client.post(self.token_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        data = {
            'title': 'Arrow of God',
            'publication_year': 1964,
            'author': self.author.id
        }
        response = self.client.post(self.token_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Things Fall Apart - Updated'}
        response = self.client.patch(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Things Fall Apart - Updated')

    def test_delete_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_search_books(self):
        response = self.client.get(self.list_url + '?search=Fall')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Things Fall Apart', str(response.data))

    def test_order_books(self):
        Book.objects.create(title='A Book', publication_year=2000, author=self.author)
        response = self.client.get(self.list_url + '?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))