from django.shortcuts import render
from products.models import BookCategory, Book


# Create your views here.

# created a controller to show the page
def index(request):
    context = {
        'title': 'Homepage'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Book Catalogue',
        'categories': BookCategory.objects.all(),
        'products': Book.objects.all(),
    }
    return render(request, 'products/products.html', context)

# maybe its better to add it via ORM?
# def books(request):
#     context = {
#         'products': [
#             {'name': 'Klara and the Sun', 'price': 20},
#             {'name': 'The Four Winds', 'price': 18},
#             {'name': 'adidas Original Black Monogram Hoodies', 'price': 80},
#             {'name': 'adidas Original Black Monogram Hoodies', 'price': 80},
#             {'name': 'adidas Original Black Monogram Hoodies', 'price': 80},
#             {'name': 'adidas Original Black Monogram Hoodies', 'price': 80},
#         ]
#
#     }
