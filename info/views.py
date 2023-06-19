from django.shortcuts import render, redirect
from .models import Book
from .form import addBookForm

# Create your views here.


def index(requset):
    books = Book.objects.all()

    return render(requset, template_name="index.html", context={"books": books})


def catalog_book(requset):
    books = Book.objects.all()
    return render(requset, template_name="catalog_list.html", context={"books": books})


def book_detail(request, pk):
    book_id = Book.objects.get(pk=pk)

    return render(request, template_name="book_detail.html", context={"book": book_id})


def add_book(request):
    if request.method == "POST":
        form = addBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = addBookForm()

    return render(request, template_name="add_book.html", context={"form": form})
