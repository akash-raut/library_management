from django.shortcuts import render
from .models import Book, Author


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'book/home.html', context)


def about(request):
    return render(request, 'book/about.html', {'title': 'About'})

