from django import forms
from .models import Book


class addBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name", "genre", "author", "amount", "image"]
