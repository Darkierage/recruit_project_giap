from rest_framework import generics
from rest_framework.response import Response

from .models import Publisher, Author, Book
from .serializers import PublisherSerializer, AuthorSerializer, BookSerializer, BookDetailsSerializer, \
    BookListSerializer, AuthorDetailsSerializer


class PublisherV(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class AuthorV(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        if kwargs:
            author = Author.objects.get(id=kwargs['pk'])
            serializer = AuthorDetailsSerializer(author)
            return Response(serializer.data)
        else:
            return self.list(request, *args, **kwargs)


class BookV(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        if kwargs:
            book = Book.objects.get(id=kwargs['pk'])
            serializer = BookDetailsSerializer(book)
            return Response(serializer.data)
        else:
            books = Book.objects.all()
            serializer = BookListSerializer(books, many=True)
            return Response(serializer.data)
