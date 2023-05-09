from django.contrib import admin

from products.models import BookCategory, Book

# Register your models here.
# registering models so that they appear in admin panel

admin.site.register(BookCategory)
admin.site.register(Book)

