# 7 make views
from django.shortcuts import render
from django.http import Http404
from .models import Book


def Home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})


def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404('Book not found')
    return render(request, 'book_detail.html', {'book': book})
