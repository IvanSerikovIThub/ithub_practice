from django.db import models
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название книги")
    genre = models.CharField(max_length=50, verbose_name="Жанр книги")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    amount = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])
