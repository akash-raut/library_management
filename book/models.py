from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


# title, image, author, description, price, file, librarian.
class Book(models.Model):
    ''' Contains book fields '''
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    librarian = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='book_default.jpeg', upload_to='book_images')
    file = models.FileField(upload_to='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title


# id, name, email, contact number
class Author(models.Model):
    ''' Contains author fields '''
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    contact = PhoneField(blank=True)
    image = models.ImageField(default='author_default.jpeg', upload_to='author_images')
    books = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def books_written(self):
        return ", ".join([str(p) for p in self.books.all()])

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.name

