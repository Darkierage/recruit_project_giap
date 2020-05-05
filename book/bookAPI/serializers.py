from rest_framework import serializers

from .models import Publisher, Author, Book


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = 'name',


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'firstname', 'lastname', 'nickname', 'birthdate')


class BookSerializer(serializers.ModelSerializer):
    publisher_name = serializers.CharField(source='publisher.name', read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'publisher_name', 'cover_image', 'pages_num', 'authors', 'publisher')


class BookDetailsSerializer(serializers.ModelSerializer):
    publisher_name = serializers.CharField(source='publisher.name')

    class Meta:
        model = Book
        fields = ('id', 'title', 'publisher_name', 'cover_image', 'pages_num')


class BookListSerializer(serializers.ModelSerializer):
    publisher_name = serializers.CharField(source='publisher.name')

    class Meta:
        model = Book
        fields = ('id', 'title', 'publisher_name', 'cover_image')


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = 'title',


class AuthorDetailsSerializer(serializers.ModelSerializer):
    books = BookAuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Author
        fields = ('id', 'firstname', 'lastname', 'nickname', 'birthdate', 'books')
