from django.urls import path
from .views import AuthorListCreateAPIView, GenreListCreateAPIView, BookListCreateAPIView,AuthorDetailView,GenreDetailAPIView,BookDetailAPIView

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('genres/', GenreListCreateAPIView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view(), name='genre-detail'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]
