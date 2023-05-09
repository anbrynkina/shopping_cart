from django.db import models

# Create your models here.

class BookCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    published_date = models.DateField()
    image = models.ImageField(upload_to='products_images', blank=True)
    # a description that will appear when you go to this product
    # description = models.TextField(blank=True)
    short_description = models.CharField(max_length=200, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(BookCategory, on_delete=models.PROTECT)

    # def __str__(self):
    #     return self.title