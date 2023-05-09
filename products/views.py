from django.shortcuts import render

# Create your views here.

# created a controller to show the page
def index(request):
    context = {
        'title': 'Homepage'
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Book Catalogue'
    }
    return render(request, 'products/products.html', context)

# maybe its better to add it via ORM?
def books(request):
    context = {
        'products': [
            {'name': 'Klara and the Sun', 'price': 20},
            {'name': 'The Four Winds', 'price': 18},
            {'name': 'adidas Original Black Monogram Hoodies', 'price': 80},
            {'name': 'adidas Original Black Monogram Hoodies', 'price': 80},
            {'name': 'adidas Original Black Monogram Hoodies', 'price': 80},
            {'name': 'adidas Original Black Monogram Hoodies', 'price': 80},
        ]

    }

# to test how dynamic content works, creating test function
def test_context(request):
    context = {
        'title': 'book store',
        'header': 'Welcome to the store!',
        'username': 'Anna',
        'products': [
            {'name': 'adidas Original Black Monogram Hoodies', 'price': 80},
            {'name': 'The North Face blue jacket', 'price': 100},
            {'name': 'ASOS DESIGN oversize sports top in brown', 'price': 59.9},
        ],
        # 'promotion': True,
        'products_of_promotion': [
            {'name': 'Nike Black Heritage Backpack', 'price': 69},
        ]
    }
    return render(request, 'products/test_context.html', context)
