from django.shortcuts import render


books = [
    {
        'author': 'Akash Raut',
        'title': 'Book Title 1',
        'content': 'First book content',
        'date_posted': 'August 15, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Book Title 2',
        'content': 'Second book content',
        'date_posted': 'August 12, 2020'
    }
]


def home(request):
    context = {
        'books': books
    }
    return render(request, 'book/home.html', context)


def about(request):
    return render(request, 'book/about.html', {'title': 'About'})

