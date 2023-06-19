from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("catalog_book", views.catalog_book, name="catalog_book"),
    path("catalog_book/<int:pk>", views.book_detail, name="book-detail"),
    path("addbook", views.add_book, name="add_book"),
]
