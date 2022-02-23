from django.db import models

# Create your models here.


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    book = models.CharField(max_length=200)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    released_at = models.DateField('date published')

    def __str__(self):
        return self.book
