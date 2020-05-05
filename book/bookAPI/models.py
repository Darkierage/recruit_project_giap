from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    birthdate = models.DateField()

    def __str__(self):
        return self.nickname


class Book(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey('publisher', on_delete=models.PROTECT)
    pages_num = models.IntegerField()
    cover_image = models.ImageField()
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return self.title
