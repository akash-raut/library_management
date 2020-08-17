from django.contrib import admin

from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'librarian')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'books_written')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
