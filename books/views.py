
from rest_framework.response import Response
from rest_framework.views import APIView
from books.models import Author, Genre, Book
from books.serializers import AuthorSerializer, GenreSerializer, BookSerializer

class AuthorListCreateAPIView(APIView):
    def get(self, request, pk):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def get(self, request, pk):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AuthorDetailView(APIView):
    def get(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        author = Author.object.get(pk=pk)
        author.delete()
        return Response(status=204)

class GenreListCreateAPIView(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class GenreDetailAPIView(APIView):
    def get(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response(status=204)

class BookListCreateAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = Book.ojects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = Book.ojects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        book = Book.ojects.get(pk=pk)
        book.delete()
        return Response(status=204)
