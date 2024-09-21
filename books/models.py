from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    description = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title
