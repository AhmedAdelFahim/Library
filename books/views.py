from django.shortcuts import render
from uuid import uuid4
import json
# Create your views here.
# books = [{"id": str(uuid4()), "title": "AAA", "author": "Ahmed", "img": "img/book1.jpg"},
#          {"id": str(uuid4()), "title": "LLL", "author": "ALi", "img": "img/book2.jpg"}]

def all_books():
    with open(".data/books", "r") as read_file:
        books = json.load(read_file)
    return books

def index(req):
    books = all_books()
    context = {
        "books": [{"title": book['title'], "id": book["id"]} for book in books]
    }
    return render(req, 'books/index.html', context)


def show(req, id):
    books = all_books()
    context = {"book": [book for book in books if str(id) == str(book['id'])][0]}
    return render(req, 'books/book.html', context)
